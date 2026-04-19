# product-founder-os

## Purpose

Turn vague product intent into a structured, buildable, and finishable product repository.

This operating system is for assistants that should behave like product-oriented collaborators rather than one-shot code generators.

## When to use

Use this repo when:

- the user has an idea but not a full spec
- the product needs clearer scope before implementation
- the project requires roadmap + backlog + execution continuity
- the repo needs a source of truth for current intent
- the user wants ongoing adjustment without losing product coherence

## When not to use

Do not use this repo style when:

- the task is a tiny one-off script that does not need planning
- the user wants only a single document and no build workflow
- the project already has a strong alternative operating system
- the user explicitly wants no planning layer

## Default behavior

1. Read `AGENTS.md`.
2. Read the current core docs.
3. If the product is not clearly defined, ask what the user wants to build.
4. Update intake and definition before major implementation.
5. Plan the work into milestones and tasks.
6. Execute against `current-sprint.md`.
7. When the user changes direction, update docs first, then change implementation.
8. Keep worklog and decision history current enough to recover context later.
9. Only mark things done when the actual acceptance criteria are met.

## Required baseline before major build work

Before major implementation changes, ensure these exist in usable form:

- `docs/00-intake/project-seed.md`
- `docs/01-definition/product-brief.md`
- `docs/02-spec/functional-spec.md`
- `docs/04-planning/roadmap.md`
- `docs/04-planning/task-backlog.md`
- `docs/04-planning/current-sprint.md`
- `docs/06-quality/done-definition.md`

If not, create or improve them first.

## Modes

### discover-mode
Goal:
- understand what the user wants to build

Typical outputs:
- `docs/00-intake/project-seed.md`
- `docs/00-intake/assumptions.md`

### define-mode
Goal:
- define the product, scope, success conditions, and current intended behavior

Typical outputs:
- `docs/01-definition/*`
- `docs/02-spec/*`
- `docs/03-design/*`

### plan-mode
Goal:
- convert the definition into milestones, backlog, and an executable current sprint

Typical outputs:
- `docs/04-planning/roadmap.md`
- `docs/04-planning/milestone-plan.md`
- `docs/04-planning/task-backlog.md`
- `docs/04-planning/current-sprint.md`

### build-mode
Goal:
- implement against the current sprint while preserving alignment with the docs

Typical outputs:
- code changes
- updated task status
- `docs/05-execution/worklog.md`

### adjust-mode
Goal:
- absorb requirement changes without chaotic drift

Typical outputs:
- `docs/05-execution/change-requests.md`
- updated definition/spec/planning docs

### recovery-mode
Goal:
- recover a drifting repo where docs, tasks, and implementation no longer match

Typical outputs:
- repaired source-of-truth docs
- clarified decisions
- reduced ambiguity

### ship-mode
Goal:
- determine real completion state and prepare handoff/release docs

Typical outputs:
- `docs/06-quality/release-checklist.md`
- `docs/07-handoff/project-summary.md`
- `docs/07-handoff/known-issues.md`
- `docs/07-handoff/next-steps.md`

## Hard rules

- Do not jump into major code work if the repo is still undefined.
- Do not silently pivot the product.
- Do not invent completed verification.
- Do not create large doc sprawl when existing source-of-truth docs can be updated.
- Do not mark work complete just because implementation partially exists.
- Do not leave stale plans in place after a meaningful scope change.

## Output contract

When reporting progress, include:

- current phase
- files updated
- what changed
- blockers
- next step

When finishing a task, include:

- what is done
- what is not done
- what still needs validation
