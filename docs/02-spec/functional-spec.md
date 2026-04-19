# Functional Spec

## Core flows
1. User says what they want to build.
2. Assistant captures the seed and assumptions.
3. Assistant creates or updates product definition docs.
4. Assistant creates or updates roadmap, backlog, and current sprint.
5. Assistant implements or guides implementation against the current sprint.
6. User changes direction.
7. Assistant records the change and updates docs before shifting implementation.
8. Assistant evaluates completion using acceptance criteria and done definition.

## Required features
- intake docs
- product brief
- scope and non-goals
- functional and UX spec
- roadmap and backlog
- current sprint
- change request tracking
- worklog and decision log
- done definition and release checklist

## Inputs
- user requests
- current repo state
- existing docs
- implementation changes

## Outputs
- updated docs
- better-aligned tasks
- implementation guidance or implementation changes
- clearer completion state

## Constraints
- must stay repo-first
- must remain readable in public
- should prefer updating source-of-truth docs over doc sprawl
