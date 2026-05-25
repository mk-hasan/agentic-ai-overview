#!/usr/bin/env python3
"""Prepend language switcher lines to English docs that have Bangla versions."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SWITCHER_EN = "> **English** | [বাংলা]({bn})\n\n"
MARKER = "> **English** | [বাংলা]"


def prepend_switcher(path: Path, bn_rel: str) -> None:
    text = path.read_text(encoding="utf-8")
    if MARKER in text[:120]:
        return
    path.write_text(SWITCHER_EN.format(bn=bn_rel) + text, encoding="utf-8")
    print(f"  updated {path.relative_to(ROOT)}")


def main() -> None:
    mappings: list[tuple[Path, str]] = [
        (ROOT / "README.md", "README.bn.md"),
        (ROOT / "docs/getting-started.md", "bn/getting-started.md"),
        (ROOT / "docs/architecture/overview.md", "../bn/architecture/overview.md"),
        (ROOT / "docs/architecture/langgraph.md", "../bn/architecture/langgraph.md"),
        (ROOT / "docs/architecture/single-vs-multi-agent.md", "../bn/architecture/single-vs-multi-agent.md"),
        (ROOT / "docs/architecture/mcp.md", "../bn/architecture/mcp.md"),
        (ROOT / "docs/patterns/README.md", "../bn/patterns/README.md"),
        (ROOT / "docs/patterns/glossary.md", "../bn/patterns/glossary.md"),
        (ROOT / "docs/use-cases/README.md", "../bn/use-cases/README.md"),
        (ROOT / "docs/use-cases/it-helpdesk.md", "../bn/use-cases/it-helpdesk.md"),
        (ROOT / "docs/use-cases/ecommerce-order-support.md", "../bn/use-cases/ecommerce-order-support.md"),
        (ROOT / "docs/use-cases/demand-forecast.md", "../bn/use-cases/demand-forecast.md"),
        (ROOT / "docs/use-cases/run-all-examples.md", "../bn/use-cases/run-all-examples.md"),
        (ROOT / "patterns/README.md", "README.bn.md"),
    ]

    for path, bn in mappings:
        if path.exists():
            prepend_switcher(path, bn)

    for pattern_dir in sorted((ROOT / "patterns").glob("*")):
        if not pattern_dir.is_dir() or pattern_dir.name == "README.md":
            continue
        readme = pattern_dir / "README.md"
        if readme.exists():
            prepend_switcher(readme, "README.bn.md")
        use_case = pattern_dir / "use-case.md"
        if use_case.exists():
            prepend_switcher(use_case, "use-case.bn.md")
        example = pattern_dir / "example"
        if example.is_dir():
            ex_readme = example / "README.md"
            if ex_readme.exists():
                prepend_switcher(ex_readme, "README.bn.md")
            for scenario in ("helpdesk", "ecommerce", "demand-forecast"):
                sreadme = example / scenario / "README.md"
                if sreadme.exists():
                    prepend_switcher(sreadme, "README.bn.md")


if __name__ == "__main__":
    main()
    print("Done.")
