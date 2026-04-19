#!/usr/bin/env python3
from pathlib import Path
import argparse
import re

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "new-product"

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main() -> int:
    parser = argparse.ArgumentParser(description="Create starter docs for a new product idea.")
    parser.add_argument("name", help="Product name")
    parser.add_argument("--one-line", default="Not defined yet.", help="One-line description")
    parser.add_argument("--user", default="Not defined yet.", help="Primary user")
    args = parser.parse_args()

    slug = slugify(args.name)
    root = Path("generated") / slug

    write(root / "project-seed.md", f"""# Project Seed

## Current idea
{args.name}

## Who it is for
{args.user}

## Problem
Not defined yet.

## MVP target
Not defined yet.

## Constraints
Not defined yet.
""")

    write(root / "product-brief.md", f"""# Product Brief

## Product
{args.name}

## One-line description
{args.one_line}

## Primary user
{args.user}

## Primary value
Not defined yet.

## MVP
Not defined yet.
""")

    write(root / "functional-spec.md", """# Functional Spec

## Core flows
Not defined yet.

## Required features
Not defined yet.

## Inputs
Not defined yet.

## Outputs
Not defined yet.

## Constraints
Not defined yet.
""")

    write(root / "roadmap.md", """# Roadmap

## Milestone 1
Define the product clearly.

## Milestone 2
Plan the first executable increment.

## Milestone 3
Implement the first useful version.
""")

    write(root / "current-sprint.md", """# Current Sprint

## Goal
Create the first usable product baseline.

## Tasks
- fill the brief
- fill the functional spec
- define acceptance criteria
- define the first implementation slice
""")

    write(root / "done-definition.md", """# Done Definition

The current increment is done when:
- the planned scope is implemented
- the acceptance criteria are met
- remaining gaps are documented
""")

    print(f"Created starter product docs under: {root}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
