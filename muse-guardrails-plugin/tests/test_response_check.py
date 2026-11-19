import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/muse-api-integration-check/scripts/muse_response_check.py'
sys.path.insert(0, str(SCRIPT.parent))
from muse_response_check import check_response


def chat(text='Answer', calls=None, finish='stop'):
    message = dict(role='assistant', content=text)
    if calls is not None:
        message['tool_calls'] = calls
    return dict(choices=[dict(message=message, finish_reason=finish)])


def tool(name='search', args=None):
    return dict(type='function', function=dict(name=name, arguments=json.dumps(args if args is not None else {})))


def codes(result):
    return {f['code'] for f in result['flags']}


class ResponseCheckTests(unittest.TestCase):
    def test_issue_modelled_fixtures(self):
        for path in sorted((ROOT / 'tests/fixtures').glob('*.json')):
            with self.subTest(fixture=path.name):
                fixture = json.loads(path.read_text())
                self.assertTrue(fixture['synthetic'])
                self.assertTrue(fixture['source'].startswith('https://github.com/'))
                result = check_response(**fixture['input'])
                self.assertFalse(result['ok'])
                self.assertTrue(set(fixture['expected_codes']) <= codes(result))

    def test_chat_responses_text_and_refusals(self):
        for response in [chat(), dict(status='completed', output=[dict(type='message', content=[dict(type='output_text', text='Answer')])])]:
            result = check_response(response)
            self.assertTrue(result['ok'])
            self.assertEqual(result['visible_text'], 'Answer')
            self.assertFalse(result['flags'])
        response = chat(None)
        response['choices'][0]['message']['refusal'] = 'I cannot determine that.'
        self.assertTrue(check_response(response)['ok'])
        response = dict(output=[dict(type='message', content=[dict(type='refusal', refusal='Declined')])])
        self.assertEqual(check_response(response)['visible_text'], 'Declined')

    def test_tool_only_continuation_not_empty_failure(self):
        response = chat(None, [tool()])
        result = check_response(response, declared_tools=['search'], tool_schemas={'search': {'type': 'object'}})
        self.assertTrue(result['ok'])
        self.assertEqual(result['flags'], [dict(code='empty_visible_content', path='$.choices[0]', severity='info')])
        self.assertEqual(result['tool_calls'][0]['arguments'], {})
        self.assertTrue(result['tool_calls'][0]['schema_checked'])

    def test_safe_opt_in_coercion_and_input_purity(self):
        payload = json.loads((ROOT / 'tests/fixtures/whole_float.json').read_text())['input']
        payload['coerce_whole_floats'] = True
        original = copy.deepcopy(payload)
        with patch('builtins.open', side_effect=AssertionError('pure function must not read files')):
            result = check_response(**payload)
        self.assertTrue(result['ok'])
        self.assertEqual(result['coercions'][0]['before'], 8.0)
        self.assertIs(type(result['tool_calls'][0]['arguments']['limit']), int)
        self.assertIn('integer_value_coerced', codes(result))
        self.assertEqual(payload, original)

    def test_nested_integer_arrays_bounds_and_type_errors(self):
        schema = {'type': 'object', 'properties': {'items': {'type': 'array', 'items': {'type': 'object', 'properties': {'limit': {'type': 'integer', 'minimum': 0, 'maximum': 10}}}}}}
        for value in [8.5, True, '8', None, float('inf'), float('nan'), float(2**53), -1.0, 11.0]:
            with self.subTest(value=value):
                call = tool()
                call['function']['arguments'] = {'items': [{'limit': value}]}
                result = check_response(chat(None, [call]), ['search'], {'search': schema}, True)
                self.assertFalse(result['ok'])
                self.assertTrue({'integer_type_mismatch', 'argument_out_of_bounds'} & codes(result))
        result = check_response(chat(None, [tool(args={'items': [{'limit': 8.0}]})]), ['search'], {'search': schema}, True)
        self.assertTrue(result['ok'])
        self.assertEqual(result['coercions'][0]['path'], '$.choices[0].message.tool_calls[0].arguments.items[0].limit')

    def test_integer_exact_large_values_and_negative_whole_float(self):
        for value in [-(2**60), 2**60, -3.0]:
            result = check_response(chat(None, [tool(args={'n': value})]), ['search'],
                                    {'search': {'properties': {'n': {'type': 'integer'}}}}, True)
            self.assertTrue(result['ok'])
            self.assertEqual(result['tool_calls'][0]['arguments']['n'], int(value))

    def test_schema_enum_equality_required_only_and_untyped_bounds(self):
        for value in [1, 1.0, {'n': 1.0}, [1.0]]:
            expected = {'n': 1} if isinstance(value, dict) else [1] if isinstance(value, list) else 1
            schema = {'properties': {'n': {'enum': [expected]}}}
            self.assertTrue(check_response(chat(None, [tool(args={'n': value})]), ['search'], {'search': schema})['ok'])
        schema = {'properties': {'n': {'enum': [1]}}}
        self.assertIn('enum_mismatch', codes(check_response(chat(None, [tool(args={'n': True})]), ['search'], {'search': schema})))
        self.assertIn('missing_required_argument', codes(check_response(chat(None, [tool()]), ['search'], {'search': {'required': ['n']}})))
        self.assertIn('argument_out_of_bounds', codes(check_response(chat(None, [tool(args={'n': -1})]), ['search'], {'search': {'properties': {'n': {'minimum': 0}}}})))

    def test_ambiguous_protocol_is_not_silently_accepted(self):
        result = check_response(chat() | {'output': []})
        self.assertFalse(result['ok'])
        self.assertIn('ambiguous_protocol', codes(result))

    def test_tool_names_not_repaired_and_declarations_required(self):
        for declarations in [None, [], ['other'], ['default.search']]:
            self.assertFalse(check_response(chat(None, [tool()]), declarations)['ok'])
        result = check_response(chat(None, [tool()]), ['search'])
        self.assertTrue(result['ok'])
        self.assertIn('tool_schema_unavailable', codes(result))
        self.assertFalse(result['tool_calls'][0]['schema_checked'])

    def test_arguments_empty_malformed_required_additional_schema(self):
        for raw in ['', '{', '[]', 'null', 'true', '7', None]:
            call = tool()
            call['function']['arguments'] = raw
            self.assertIn('malformed_tool_arguments', codes(check_response(chat(None, [call]), ['search'])))
        schema = {'type': 'object', 'properties': {'limit': {'type': 'integer'}}, 'required': ['limit'], 'additionalProperties': False}
        result = check_response(chat(None, [tool(args={'extra': 1})]), ['search'], {'search': schema})
        self.assertTrue({'missing_required_argument', 'additional_argument'} <= codes(result))
        for schema in [{'anyOf': [{'type': 'integer'}]}, {'type': ['integer', 'null']}, {'properties': {'n': {'type': 'integer', 'exclusiveMinimum': 0}}}]:
            self.assertIn('unsupported_schema', codes(check_response(chat(None, [tool(args={'n': 1})]), ['search'], {'search': schema})))

    def test_markup_detection_dangling_tags_and_fenced_explanations(self):
        for text in ['</atem:function>', '<atem:function_calls>', '<tool_call>', '[TOOL_CALLS]', '<|tool_call|>']:
            self.assertIn('tool_call_as_text', codes(check_response(chat(text))))
        self.assertTrue(check_response(chat('Example only:\n```xml\n</atem:function>\n```'))['ok'])
        self.assertTrue(check_response(chat('I can explain tool calls.'))['ok'])

    def test_empty_unknown_malformed_and_incomplete_responses(self):
        for response in [None, [], {}, {'choices': []}, {'choices': [None]}, {'output': None},
                         {'output': [None]}, {'output': [{'type': 'unknown'}]}, chat(' \n'),
                         {'output': [{'type': 'reasoning', 'summary': [{'text': 'not a visible answer'}]}]},
                         {'status': 'in_progress', 'output': []}]:
            with self.subTest(response=response):
                self.assertFalse(check_response(response)['ok'])
        self.assertIn('finish_reason_length', codes(check_response(chat('partial', finish='length'))))
        self.assertFalse(check_response({'status': 'incomplete', 'output': [{'type': 'message', 'content': 'partial'}]})['ok'])

    def test_invalid_configuration(self):
        for kwargs in [dict(declared_tools='search'), dict(declared_tools=['search', 'search']),
                       dict(declared_tools=[1]), dict(tool_schemas=[]), dict(tool_schemas={'search': False}),
                       dict(coerce_whole_floats='yes')]:
            with self.assertRaises(ValueError):
                check_response(chat(), **kwargs)

    def test_cli_json_stdin_file_help_and_exit_codes(self):
        def run(args, stdin=None):
            return subprocess.run([sys.executable, str(SCRIPT), *args], input=stdin, text=True, capture_output=True)
        self.assertEqual(run(['--help']).returncode, 0)
        good = json.dumps({'response': chat()})
        for args, stdin in [(['--json', good], None), (['--json', '-'], good)]:
            result = run(args, stdin)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)['ok'])
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'input.json'
            path.write_text(good)
            self.assertEqual(run(['--json', str(path)]).returncode, 0)
        result = run(['--json', json.dumps({'response': chat('')})])
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)['ok'])
        for value in ['{', '{}', '{"response":NaN}', '{"response":{},"unknown":true}', good + '\ndata: [DONE]']:
            self.assertEqual(run(['--json', value]).returncode, 2)


if __name__ == '__main__':
    unittest.main()
