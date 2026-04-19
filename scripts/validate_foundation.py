#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

required_files = [
    "README.md",
    "SKILL.md",
    "AGENTS.md",
    "docs/00-intake/project-seed.md",
    "docs/01-definition/product-brief.md",
    "docs/02-spec/functional-spec.md",
    "docs/04-planning/roadmap.md",
    "docs/04-planning/task-backlog.md",
    "docs/04-planning/current-sprint.md",
    "docs/06-quality/done-definition.md",
]

placeholder_markers = [
    "Not filled yet.",
    "Not defined yet.",
    "No tasks yet.",
    "No active sprint yet.",
    "No milestones defined yet.",
    "No non-goals recorded yet.",
    "No assumptions recorded yet.",
]

core_scan_roots = [
    ROOT / "README.md",
    ROOT / "SKILL.md",
    ROOT / "AGENTS.md",
    ROOT / "docs",
]

def iter_core_markdown():
    for item in core_scan_roots:
        if item.is_file():
            yield item
        elif item.is_dir():
            for path in item.rglob("*.md"):
                yield path

def main() -> int:
    missing = []
    placeholder_hits = []
    fence_errors = []

    for rel in required_files:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)

    for path in iter_core_markdown():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        if "templates/" in str(rel):
            continue
        for marker in placeholder_markers:
            if marker in text:
                placeholder_hits.append(f"{rel}: {marker}")
        if text.count("```") % 2 != 0:
            fence_errors.append(str(rel))

    if missing:
        print("Missing required files:")
        for rel in missing:
            print(f"- {rel}")

    if placeholder_hits:
        print("Placeholder markers found:")
        for hit in placeholder_hits:
            print(f"- {hit}")

    if fence_errors:
        print("Malformed markdown code fences found:")
        for rel in fence_errors:
            print(f"- {rel}")

    if missing or placeholder_hits or fence_errors:
        return 1

    print("Foundation files exist and no obvious placeholder/fence issues were found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
