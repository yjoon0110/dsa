# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What This Repo Is

A personal DSA interview prep workspace. Python solutions are written one-per-file in topic folders and run directly — no build system, no test framework, no CI.

## Running Solutions

```bash
python Arrays/two_sum.py
```

Each file is self-contained with test cases at the bottom (`print(...)` assertions). Run the file to verify.

## Repo Workflow

1. Pick the next problem from `problems.md` (current week's unchecked item)
2. Create a `.py` file in the appropriate topic folder (e.g., `Arrays/`, `03_hash_maps/`)
3. Solve it — follow the 6-step template below
4. Log the result in `progress.md` (date, problem, pattern, time, hint needed, key insight)
5. Check off the problem in `problems.md`

## The Problem-Solving Template (mandatory before any code)

```
1. UNDERSTAND    — Restate in your own words. Inputs/outputs? Constraints? Edge cases?
2. PATTERN MATCH — Which pattern applies? (see plan.md cheat sheet)
3. BRUTE FORCE   — Describe the naive solution. O(n²) is fine as a starting point.
4. OPTIMIZE      — What's the bottleneck? Hash map / two pointers / monotonic stack?
5. CODE          — Write code only after the approach is clear.
6. TEST          — Walk through 2–3 examples by hand. Include empty input and single-element.
```

## Folder Structure (planned, not all created yet)

Topic folders are created as each week's problems begin:

| Folder | Topic |
|--------|-------|
| `Arrays/` | Early warmup problems |
| `03_hash_maps/` | Week 2 — Arrays + Hashing |
| `04_stacks_queues/` | Week 4 |
| `05_linked_lists/` | Week 5 |
| `06_trees/` | Week 6 |
| `07_binary_search/` | Week 4 |
| `09_recursion_backtracking/` | Week 5 |
| `10_dynamic_programming/` | Week 8 |
| `11_graphs/` | Week 7 |

## Coaching Style

**Never give direct solutions.** This repo exists for learning through struggle. When asked for help on a problem:
- Ask what step of the template the user is stuck on
- Give a targeted hint (not the answer) — e.g., "what data structure gives O(1) lookup?"
- If a solution is shown, explain the *why* behind each decision, not just the *what*

The VS Code autocomplete and Copilot are intentionally disabled in `.vscode/settings.json` — preserve this.

## Key Files

| File | Role |
|------|------|
| `problems.md` | Week-by-week problem list with checkboxes — source of truth for what to do next |
| `progress.md` | Personal log — update after every problem |
| `plan.md` | Problem-solving template + pattern cheat sheet + daily session structure |
