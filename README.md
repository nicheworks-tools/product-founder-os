# product-founder-os

A repo operating system for turning a vague product idea into a buildable, tracked, and finishable product.

`product-founder-os` is designed for workflows where GPT and/or Codex are connected to a repository and used not just to edit code, but to move a product from idea -> definition -> plan -> implementation -> adjustment -> completion.

This repo is not a prompt dump.
It is a working structure for product development.

## What this repo is for

Use this repo when you want the assistant to:

- ask what the user wants to build
- turn that into a product brief and spec
- create and maintain a roadmap and backlog
- track decisions and change requests
- keep docs and implementation aligned
- continue toward completion instead of improvising every session

## Why this exists

Most AI-assisted repos fail for simple reasons:

- implementation starts before the product is defined
- docs drift away from reality
- requirement changes are handled informally
- tasks are not grounded in a current plan
- “done” is claimed long before completion is real

This repo exists to reduce that drift.

## Core workflow

1. Ask the user what they want to build.
2. Capture the idea in intake docs.
3. Define the product clearly.
4. Break the work into milestones and tasks.
5. Implement against the current sprint.
6. When requirements change, update docs first.
7. Only mark work done when the acceptance criteria are actually satisfied.

## 3-minute quickstart

1. Connect GPT and/or Codex to the repo.
2. Ask it to read `AGENTS.md`, `SKILL.md`, and the current docs.
3. If the repo is still undefined, have it ask what should be built.
4. Have it update:
   - `docs/00-intake/project-seed.md`
   - `docs/01-definition/product-brief.md`
   - `docs/02-spec/functional-spec.md`
   - `docs/04-planning/roadmap.md`
   - `docs/04-planning/task-backlog.md`
   - `docs/04-planning/current-sprint.md`
   - `docs/06-quality/done-definition.md`
5. Only then start major implementation work.

## Suggested first prompt

Read AGENTS.md and the current docs.
If the product is not clearly defined yet, ask me what I want to build.
Then create or update the intake docs, product brief, functional spec, roadmap, task backlog, current sprint, and done definition before making major implementation changes.

## Repo structure

- `docs/00-intake/`
  - initial idea capture
  - assumptions
  - user answers
- `docs/01-definition/`
  - product brief
  - target user
  - problem statement
  - success criteria
  - scope / non-goals
- `docs/02-spec/`
  - functional spec
  - UX spec
  - data model
  - states and errors
  - acceptance criteria
- `docs/03-design/`
  - design principles
  - UI structure
  - recurring component rules
  - copy rules
- `docs/04-planning/`
  - roadmap
  - milestones
  - backlog
  - current sprint
  - release plan
- `docs/05-execution/`
  - worklog
  - decision log
  - blockers
  - change requests
- `docs/06-quality/`
  - done definition
  - test strategy
  - QA checklist
  - release checklist
- `docs/07-handoff/`
  - project summary
  - setup/run
  - known issues
  - next steps
- `examples/`
  - one worked static-tool example
  - SaaS and content-site starter examples
- `scripts/`
  - foundation checks
  - doc link checks
  - repo status helper
  - starter bootstrap helper

## Included tooling

- `scripts/create_project_docs.py`
  - checks that the baseline operating docs exist
- `scripts/check_doc_links.py`
  - checks local markdown links
- `scripts/validate_foundation.py`
  - checks for missing core files, obvious placeholders, and malformed markdown code fences
- `scripts/bootstrap_new_product.py`
  - creates a starter seed/brief/spec/plan package for a new product idea

## Minimal baseline before major build work

At minimum, these files should be usable and current:

- `docs/00-intake/project-seed.md`
- `docs/01-definition/product-brief.md`
- `docs/02-spec/functional-spec.md`
- `docs/04-planning/roadmap.md`
- `docs/04-planning/task-backlog.md`
- `docs/04-planning/current-sprint.md`
- `docs/06-quality/done-definition.md`

## Worked example

The strongest example in this repo is:

- `examples/example-static-tool/`

It includes a small but coherent product seed, brief, functional spec, roadmap, sprint, and done definition so the operating model can be understood without guessing.

## Good use cases

- building a small SaaS
- planning a static tool before implementation
- turning a rough idea into a structured product repo
- recovering a repo that has code but no coherent product definition
- keeping requirements, tasks, and implementation aligned across multiple sessions

## Non-goals

This repo does not automatically guarantee:

- product-market fit
- launch quality
- legal correctness
- security correctness
- performance correctness
- full delivery without human review

## Public release status

This repository is intended to be usable as an initial public release, not a private scratchpad.
It includes:

- a coherent operating model
- working validation scripts
- a fully filled baseline for the repo itself
- one worked example for a small static tool
- lighter examples for broader product shapes

## Maintainer note

This repo should stay honest, compact, and current.
It should not become a dumping ground for random docs.
