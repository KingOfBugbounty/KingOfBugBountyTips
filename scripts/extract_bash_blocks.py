"""
extract_bash_blocks.py

Purpose:
    Extract every ```bash fenced code block from one or more Markdown files
    and write each as its own .sh file, so a plain shell linter (shellcheck)
    can be run over the one-liners documented in docs/*.md. Used by the
    "Lint" GitHub Actions workflow (.github/workflows/lint.yml) — see that
    file for how this feeds into CI.

Usage:
    python3 scripts/extract_bash_blocks.py <out_dir> <file_or_dir> [more...]

    Example:
        python3 scripts/extract_bash_blocks.py /tmp/blocks docs Readme.md

Requirements:
    Python 3 standard library only.

Notes:
    - This repo's one-liners intentionally use undeclared placeholder
      variables (target.com, YOUR_API_KEY, $TARGET) and unquoted expansions
      that are fine for a copy-paste recon command but would normally be
      flagged by shellcheck's style checks. CI runs shellcheck at
      `-S error` (syntax errors only) against this output, not full style
      linting, to catch genuinely broken one-liners without false-positiving
      on intentional style choices.
"""
import pathlib
import re
import sys

FENCE_RE = re.compile(r"```bash\n(.*?)```", re.S)


def iter_markdown_files(paths):
    for p in paths:
        path = pathlib.Path(p)
        if path.is_dir():
            yield from sorted(path.rglob("*.md"))
        elif path.suffix.lower() == ".md":
            yield path


def main(argv):
    if len(argv) < 3:
        print(f"Usage: {argv[0]} <out_dir> <file_or_dir> [more...]", file=sys.stderr)
        return 2

    out_dir = pathlib.Path(argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for md_file in iter_markdown_files(argv[2:]):
        content = md_file.read_text(encoding="utf-8", errors="replace")
        for i, m in enumerate(FENCE_RE.finditer(content)):
            code = m.group(1)
            if not code.strip():
                continue
            safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", str(md_file))
            out_path = out_dir / f"{safe_name}.{i}.sh"
            out_path.write_text("#!/usr/bin/env bash\n" + code, encoding="utf-8")
            count += 1

    print(f"Extracted {count} bash block(s) into {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
