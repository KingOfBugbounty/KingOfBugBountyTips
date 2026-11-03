"""
md_to_oneliners_yaml.py

Purpose:
    One-time migration helper: parse a docs/*.md oneliner file (of the
    "CVE Discovery" shape used by docs/cve-feb-2026.md) into the structured
    data/oneliners/*.yaml format, so it can be regenerated with
    scripts/generate_oneliners_md.py instead of hand-edited as prose.

    This is a migration tool, not something that runs in CI — it exists so
    future topic files can be converted the same way without re-typing
    content by hand (and risking transcription errors).

Usage:
    python3 scripts/md_to_oneliners_yaml.py docs/cve-feb-2026.md > data/oneliners/cve-feb-2026.yaml

Requirements:
    pip install pyyaml

Expected input shape (see docs/cve-feb-2026.md):
    ## <page title>

    > <intro line(s), may span multiple `>` lines / blank `>` separators>

    ### <emoji> <Title> - <CVE-XXXX-NNNNN[ / CVE-XXXX-NNNNN...]> <Suffix>

    > **<description>**

    #### <n>. <step comment>
    ```bash
    <command>
    ```
    (repeat #### steps)

    --- (separator between entries)

    ### <Title with no CVE and no description>
    ```bash
    <command>
    ```
    (a "quick" entry: single command, no step numbering, no description)

Anything that doesn't fit this shape is preserved in the YAML as a raw
"unparsed" block so no content is silently dropped; check the output for
`type: raw` entries and fix the parser or the source file if any show up.
"""
import re
import sys

import yaml


def parse(md_text: str) -> dict:
    # Strip the nav wrapper this repo's docs/*.md files share.
    body = md_text
    body = re.sub(r"^\[← Back to README\]\([^)]+\)\s*\n+---\s*\n+", "", body)
    body = re.sub(r"\n+---\s*\n+\[← Back to README\]\([^)]+\)\s*$", "", body)

    m = re.match(r"^##\s+(.+?)\s*\n+(.*)$", body, re.S)
    if not m:
        raise ValueError("Could not find top-level '## Title' heading")
    title, rest = m.group(1), m.group(2)

    # Intro: leading blockquote lines before the first '### ' heading.
    intro_m = re.match(r"((?:^>.*\n?)+)\n*", rest, re.M)
    intro = ""
    if intro_m:
        intro_lines = [re.sub(r"^>\s?", "", l) for l in intro_m.group(1).splitlines()]
        intro = "\n".join(intro_lines).strip()
        rest = rest[intro_m.end():]

    # Split into entries on '### ' headings, keeping the heading text.
    # chunks[0] is leftover text BEFORE the first heading (should be empty
    # once the intro is fully consumed above); anything else there is
    # reported as unparsed rather than silently mis-rendered as a heading.
    chunks = re.split(r"(?m)^###\s+", rest)
    entries = []
    if chunks and chunks[0].strip():
        entries.append({"type": "raw", "content": chunks[0].strip("\n")})
    for chunk in chunks[1:]:
        if not chunk.strip():
            continue
        lines = chunk.split("\n", 1)
        heading = lines[0].strip()
        chunk_body = lines[1] if len(lines) > 1 else ""
        # drop a single trailing '---' separator line (between entries),
        # but remember whether it was there so a "quick" entry (which has
        # no separator by default) can round-trip it back.
        stripped_body, n_subs = re.subn(r"\n+---\s*$", "", chunk_body)
        had_trailing_separator = n_subs > 0
        chunk_body = stripped_body.strip("\n")

        cve_match = re.match(r"^(.*?)\s+-\s+((?:CVE-\d{4}-\d+\s*/?\s*)+)(.*)$", heading)
        desc_match = re.match(r"^\s*>\s*\*\*(.+?)\*\*\s*\n+(.*)$", chunk_body, re.S)

        if cve_match and desc_match:
            name, cve_ids_raw, suffix = cve_match.groups()
            name = re.sub(r"^⚡\s*", "", name.strip())
            cve_ids = [c.strip() for c in re.split(r"\s*/\s*", cve_ids_raw.strip())]
            description = desc_match.group(1).strip()
            steps_body = desc_match.group(2)

            steps = []
            step_chunks = re.split(r"(?m)^####\s+", steps_body)
            for sc in step_chunks:
                if not sc.strip():
                    continue
                step_lines = sc.split("\n", 1)
                step_heading = step_lines[0].strip()
                step_rest = step_lines[1] if len(step_lines) > 1 else ""
                code_m = re.search(r"```bash\n(.*?)```", step_rest, re.S)
                if not code_m:
                    entries.append({"type": "raw", "content": "#### " + sc})
                    continue
                # strip a leading "N. " step number — it's regenerated from position
                comment = re.sub(r"^\d+\.\s*", "", step_heading)
                steps.append({"comment": comment, "command": code_m.group(1).strip()})

            entries.append({
                "type": "cve",
                "title": name,
                "cve_ids": cve_ids,
                "suffix": suffix.strip(),
                "description": description,
                "steps": steps,
            })
            continue

        # "quick" shape: just a heading + one code block, no description.
        code_m = re.search(r"```bash\n(.*?)```", chunk_body, re.S)
        if code_m and chunk_body.strip().startswith("```"):
            trailing = chunk_body[code_m.end():].strip()
            if trailing:
                # Unexpected extra content after the code block — don't
                # silently drop it.
                entries.append({"type": "raw", "content": trailing})
            entry = {
                "type": "quick",
                "title": heading,
                "command": code_m.group(1).strip(),
            }
            if had_trailing_separator:
                entry["separator_after"] = True
            entries.append(entry)
            continue

        entries.append({"type": "raw", "content": "### " + chunk})

    return {"title": title, "intro": intro, "entries": entries}


def main(argv):
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <input.md>", file=sys.stderr)
        return 2
    md_text = open(argv[1], encoding="utf-8").read()
    data = parse(md_text)
    raw_count = sum(1 for e in data["entries"] if e["type"] == "raw")
    if raw_count:
        print(f"WARNING: {raw_count} unparsed 'raw' block(s) — review output", file=sys.stderr)
    yaml.dump(data, sys.stdout, sort_keys=False, allow_unicode=True, width=100)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
