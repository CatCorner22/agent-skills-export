#!/usr/bin/env python3
"""Export a living reference to DOCX/PDF/HTML after refreshing it.
Usage: export_reference.py FILE.md [--to docx|pdf|html] [--out PATH] [--no-refresh]
Uses pandoc via pypandoc (pip install pypandoc_binary) or a `pandoc` binary on PATH. Keeps generated blocks; strips HTML marker comments."""
import os, re, sys, shutil, subprocess, argparse

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("file"); ap.add_argument("--to", default="docx", choices=["docx", "pdf", "html"])
    ap.add_argument("--out"); ap.add_argument("--no-refresh", action="store_true"); a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    if not a.no_refresh:
        r = subprocess.run([sys.executable, os.path.join(here, "refresh_reference.py"), a.file], capture_output=True, text=True)
        if r.returncode not in (0, 1): sys.exit(r.stderr or "refresh failed")
    md = open(a.file, encoding="utf-8").read()
    md = re.sub(r"<!--\s*\w+:(start|end)\s*-->\n?", "", md)          # drop block markers
    md = re.sub(r"\{\{index:[^}]*\}\}\n?", "", md)                     # drop index tags (index block stays)
    out = a.out or os.path.splitext(a.file)[0] + "." + a.to
    args = ["--toc", "--toc-depth=3", "-s"] + (["--metadata", "title=" + re.sub(r"^#\s*", "", md.splitlines()[0])] if md.startswith("#") else [])
    try:
        import pypandoc
        pypandoc.convert_text(md, a.to, format="md", outputfile=out, extra_args=args)
    except ImportError:
        if not shutil.which("pandoc"): sys.exit("need pypandoc (pip install pypandoc_binary) or pandoc on PATH")
        subprocess.run(["pandoc", "-f", "markdown", "-t", a.to, "-o", out] + args, input=md, text=True, check=True)
    print(out)

if __name__ == "__main__": main()
