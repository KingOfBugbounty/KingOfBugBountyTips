"""
generate_oneliners_md.py

Purpose:
    Render a structured data/oneliners/*.yaml file into the Markdown shape
    used under docs/ (nav back-link, intro blockquote, CVE entries with
    numbered steps, "quick" single-command entries), so new one-liners can
    be added as structured data instead of hand-formatted prose.

Usage:
    python3 scripts/generate_oneliners_md.py data/oneliners/cve-feb-2026.yaml docs/cve-feb-2026.md
    # or print to stdout:
    python3 scripts/generate_oneliners_md.py data/oneliners/cve-feb-2026.yaml

Requirements:
    pip install pyyaml

YAML schema (see data/oneliners/cve-feb-2026.yaml for a worked example):
    title: <page title, e.g. "February 2026 CVE Discovery Oneliners">
    intro: |
      <blockquote intro text; each line becomes a "> " line>
    entries:
      - type: cve
        title: <product/component name>
        cve_ids: [CVE-YYYY-NNNNN, ...]       # one or more
        suffix: <short tail, e.g. "Discovery">
        description: <one paragraph, rendered bold in a blockquote>
        steps:
          - comment: <what this step does>
            command: <shell one-liner>
          - ...
      - type: quick
        title: <short technique name>
        command: <shell one-liner>

Regenerating a file is idempotent: running this twice on the same YAML
produces byte-identical Markdown.
"""
import sys

import yaml

NAV_BACK = "[← Back to README](../Readme.md)"


def notice_for(yaml_path: str) -> str:
    return (
        f"<!-- GENERATED FILE — do not edit by hand.\n"
        f"     Source: {yaml_path}\n"
        f"     Regenerate with: python3 scripts/generate_oneliners_md.py {yaml_path} <this file>\n"
        f"     See CONTRIBUTING.md § \"Structured one-liner data\" for how to add an entry. -->"
    )


def render_entry(entry: dict) -> str:
    if entry["type"] == "cve":
        cve_str = " / ".join(entry["cve_ids"])
        heading = f"### ⚡ {entry['title']} - {cve_str} {entry['suffix']}".rstrip()
        out = [heading, "", f"> **{entry['description']}**", ""]
        for i, step in enumerate(entry["steps"], start=1):
            out.append(f"#### {i}. {step['comment']}")
            out.append("```bash")
            out.append(step["command"])
            out.append("```")
            out.append("")
        out.append("---")
        return "\n".join(out)

    if entry["type"] == "quick":
        lines = [
            f"### {entry['title']}",
            "```bash",
            entry["command"],
            "```",
        ]
        if entry.get("separator_after"):
            lines += ["", "---"]
        return "\n".join(lines)

    if entry["type"] == "raw":
        return entry["content"].rstrip("\n")

    raise ValueError(f"Unknown entry type: {entry['type']!r}")


def render(data: dict, yaml_path: str) -> str:
    intro_lines = [f"> {l}" if l.strip() else ">" for l in data["intro"].splitlines()]
    parts = [
        NAV_BACK,
        "",
        notice_for(yaml_path),
        "",
        "---",
        "",
        f"## {data['title']}",
        "",
        "\n".join(intro_lines),
        "",
    ]
    parts.append("\n\n".join(render_entry(e) for e in data["entries"]))
    parts += ["", NAV_BACK, ""]
    return "\n".join(parts)


def main(argv):
    if len(argv) not in (2, 3):
        print(f"Usage: {argv[0]} <input.yaml> [output.md]", file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    out = render(data, argv[1])
    if len(argv) == 3:
        with open(argv[2], "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"Wrote {argv[2]}")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
