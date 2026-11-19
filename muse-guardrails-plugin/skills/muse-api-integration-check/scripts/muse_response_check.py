"""Pure, supplemental checks on completed Chat Completions/Responses JSON; no execution."""

import argparse
import copy
import json
import math
import re
import sys
from pathlib import Path

MAX_SAFE_INTEGER = 2 ** 53 - 1
SCHEMA_KEYS = {'type', 'properties', 'required', 'additionalProperties', 'items', 'minimum',
               'maximum', 'enum', 'description', 'title', 'default', '$schema'}
MARKUP = re.compile(r'</?\s*(?:atem:)?(?:function(?:_calls?)?|invoke|parameter|tool_call|tool_use)\b'
                    r'|<\|tool_call\|>|\[TOOL_CALLS\]', re.I)


def reject_constant(value):
    raise ValueError('Non-finite JSON constant: ' + value)


def load_json(text):
    return json.loads(text, parse_constant=reject_constant)


def json_equal(left, right):
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is type(right) and left == right
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(json_equal(a, b) for a, b in zip(left, right))
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(json_equal(left[k], right[k]) for k in left)
    return left == right


def check_response(response, declared_tools=None, tool_schemas=None, coerce_whole_floats=False):
    """Return flags and copied argument normalization; ok is not execution authorization."""
    if declared_tools is not None and (not isinstance(declared_tools, list)
            or any(not isinstance(n, str) or not n for n in declared_tools)
            or len(set(declared_tools)) != len(declared_tools)):
        raise ValueError('declared_tools must be a unique list of nonempty names, or null')
    if tool_schemas is None:
        tool_schemas = {}
    if not isinstance(tool_schemas, dict) or any(not isinstance(k, str) or not isinstance(v, dict)
                                               for k, v in tool_schemas.items()):
        raise ValueError('tool_schemas must map names to parameter-schema objects')
    if not isinstance(coerce_whole_floats, bool):
        raise ValueError('coerce_whole_floats must be boolean')
    flags, calls, coercions, visible = [], [], [], []
    protocol = None

    def flag(code, path, severity='error'):
        flags.append(dict(code=code, path=path, severity=severity))

    def arguments(value, schema, path):
        if not isinstance(schema, dict):
            flag('unsupported_schema', path)
            return value
        if set(schema) - SCHEMA_KEYS:
            flag('unsupported_schema', path)
        kind = schema.get('type')
        if kind is not None and kind not in ('object', 'array', 'integer', 'number', 'string', 'boolean', 'null'):
            flag('unsupported_schema', path)
            return value
        if kind == 'integer':
            if isinstance(value, float) and math.isfinite(value) and value.is_integer() and abs(value) <= MAX_SAFE_INTEGER and coerce_whole_floats:
                coercions.append(dict(path=path, before=value, after=int(value)))
                flag('integer_value_coerced', path, 'warning')
                value = int(value)
            if isinstance(value, bool) or not isinstance(value, int):
                flag('integer_type_mismatch', path)
                return value
        elif kind == 'number' and (isinstance(value, bool) or not isinstance(value, (int, float))
                                   or (isinstance(value, float) and not math.isfinite(value))):
            flag('number_type_mismatch', path)
            return value
        elif kind in ('string', 'boolean', 'null'):
            expected = {'string': str, 'boolean': bool, 'null': type(None)}[kind]
            if not isinstance(value, expected):
                flag('schema_type_mismatch', path)
                return value
        if kind == 'object' or (kind is None and any(k in schema for k in ('properties', 'required', 'additionalProperties'))):
            if not isinstance(value, dict):
                flag('schema_type_mismatch', path)
                return value
            properties = schema.get('properties', {})
            required = schema.get('required', [])
            if not isinstance(properties, dict) or not isinstance(required, list) or any(not isinstance(n, str) for n in required):
                flag('unsupported_schema', path)
                return value
            for name in required:
                if name not in value:
                    flag('missing_required_argument', path + '.' + name)
            additional = schema.get('additionalProperties', True)
            if not isinstance(additional, (bool, dict)):
                flag('unsupported_schema', path)
            for name, item in value.items():
                if name in properties:
                    value[name] = arguments(item, properties[name], path + '.' + name)
                elif additional is False:
                    flag('additional_argument', path + '.' + name)
                elif isinstance(additional, dict):
                    value[name] = arguments(item, additional, path + '.' + name)
        if kind == 'array' or (kind is None and 'items' in schema):
            if not isinstance(value, list):
                flag('schema_type_mismatch', path)
                return value
            for i, item in enumerate(value):
                value[i] = arguments(item, schema.get('items', {}), f'{path}[{i}]')
        if 'enum' in schema:
            if not isinstance(schema['enum'], list):
                flag('unsupported_schema', path)
            elif not any(json_equal(value, item) for item in schema['enum']):
                flag('enum_mismatch', path)
        if kind in ('integer', 'number') or (kind is None and isinstance(value, (int, float)) and not isinstance(value, bool)):
            for bound, predicate in (('minimum', lambda a, b: a >= b), ('maximum', lambda a, b: a <= b)):
                if bound in schema:
                    limit = schema[bound]
                    if isinstance(limit, bool) or not isinstance(limit, (int, float)) or (isinstance(limit, float) and not math.isfinite(limit)):
                        flag('unsupported_schema', path)
                    elif not predicate(value, limit):
                        flag('argument_out_of_bounds', path)
        return value

    def tool(call, path, chat=False):
        if not isinstance(call, dict):
            flag('malformed_tool_call', path)
            return
        if chat and call.get('type', 'function') != 'function':
            flag('unsupported_tool_call', path)
        function = call.get('function', call) if chat else call
        if not isinstance(function, dict) or not isinstance(function.get('name'), str) or not function['name'].strip():
            flag('malformed_tool_call', path)
            return
        name = function['name']
        if declared_tools is None:
            flag('tool_declarations_missing', path)
        elif name not in declared_tools:
            flag('undeclared_tool', path)
        raw = function.get('arguments')
        try:
            value = load_json(raw) if isinstance(raw, str) else copy.deepcopy(raw)
        except (ValueError, TypeError):
            flag('malformed_tool_arguments', path)
            return
        if not isinstance(value, dict):
            flag('malformed_tool_arguments', path)
            return
        if name in tool_schemas:
            value = arguments(value, tool_schemas[name], path + '.arguments')
        else:
            flag('tool_schema_unavailable', path, 'warning')
        calls.append(dict(name=name, arguments=value, path=path, schema_checked=name in tool_schemas))

    def content(value, path):
        parts = []
        if value is None:
            return parts
        if isinstance(value, str):
            return [value]
        if not isinstance(value, list):
            flag('malformed_visible_content', path)
            return parts
        for i, part in enumerate(value):
            if not isinstance(part, dict):
                flag('malformed_visible_content', f'{path}[{i}]')
                continue
            kind = part.get('type')
            key = 'refusal' if kind == 'refusal' else 'text'
            if kind in ('text', 'output_text', 'refusal') and isinstance(part.get(key), str):
                parts.append(part[key])
            else:
                flag('unsupported_visible_content', f'{path}[{i}]')
        return parts

    def finish_turn(parts, tool_count, path):
        text = '\n'.join(parts).strip()
        if not text:
            flag('empty_visible_content', path, 'info' if tool_count else 'error')
        unfenced = re.sub(r'```.*?```|~~~.*?~~~', '', text, flags=re.S)
        if MARKUP.search(unfenced):
            flag('tool_call_as_text', path)
        if text:
            visible.append(text)

    if not isinstance(response, dict):
        flag('malformed_response', '$')
    elif response.get('error') is not None:
        flag('upstream_error', '$.error')
    elif 'choices' in response and 'output' in response:
        flag('ambiguous_protocol', '$')
    elif 'choices' in response:
        protocol = 'chat_completions'
        choices = response['choices']
        if not isinstance(choices, list) or not choices:
            flag('malformed_response', '$.choices')
        else:
            for i, choice in enumerate(choices):
                path = f'$.choices[{i}]'
                if not isinstance(choice, dict) or not isinstance(choice.get('message'), dict):
                    flag('malformed_response', path)
                    continue
                if choice.get('finish_reason') == 'length':
                    flag('finish_reason_length', path)
                message = choice['message']
                if message.get('role', 'assistant') != 'assistant':
                    flag('unexpected_message_role', path)
                parts = content(message.get('content'), path + '.message.content')
                if isinstance(message.get('refusal'), str):
                    parts.append(message['refusal'])
                raw_calls = message.get('tool_calls', [])
                if not isinstance(raw_calls, list):
                    flag('malformed_tool_call', path)
                    raw_calls = []
                if 'function_call' in message:
                    raw_calls = raw_calls + [message['function_call']]
                before = len(calls)
                for j, call in enumerate(raw_calls):
                    tool(call, f'{path}.message.tool_calls[{j}]', chat=True)
                finish_turn(parts, len(calls) - before, path)
    elif 'output' in response:
        protocol = 'responses'
        status = response.get('status')
        incomplete = response.get('incomplete_details') or {}
        if not isinstance(incomplete, dict):
            flag('malformed_response', '$.incomplete_details')
            incomplete = {}
        if incomplete.get('reason') in ('max_output_tokens', 'max_tokens', 'length'):
            flag('finish_reason_length', '$.incomplete_details')
        if status is not None and status != 'completed':
            flag('incomplete_response', '$.status')
        output = response['output']
        parts = []
        if not isinstance(output, list):
            flag('malformed_response', '$.output')
        else:
            for i, item in enumerate(output):
                path = f'$.output[{i}]'
                if not isinstance(item, dict):
                    flag('malformed_response', path)
                elif item.get('type') == 'message':
                    if item.get('role', 'assistant') != 'assistant':
                        flag('unexpected_message_role', path)
                    parts += content(item.get('content'), path + '.content')
                elif item.get('type') == 'function_call':
                    tool(item, path)
                elif item.get('type') != 'reasoning':
                    flag('unsupported_output_item', path)
        finish_turn(parts, len(calls), '$.output')
    else:
        flag('unrecognized_protocol', '$')
    if not visible and not any(f['code'] == 'empty_visible_content' for f in flags):
        flag('empty_visible_content', '$')
    return dict(ok=not any(f['severity'] == 'error' for f in flags), protocol=protocol,
                visible_text='\n'.join(visible), flags=flags, tool_calls=calls, coercions=coercions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', required=True, help='JSON envelope, input file, or - for stdin')
    args = parser.parse_args()
    try:
        source = args.json
        payload = load_json(sys.stdin.read() if source == '-' else source if source.lstrip().startswith('{') else Path(source).read_text())
        if not isinstance(payload, dict) or 'response' not in payload:
            raise ValueError('Input must be an object containing response')
        if set(payload) - {'response', 'declared_tools', 'tool_schemas', 'coerce_whole_floats'}:
            raise ValueError('Unrecognized configuration field')
        result = check_response(**payload)
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0 if result['ok'] else 1
    except (ValueError, OSError, TypeError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
