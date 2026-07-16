# DSA Study Plan

## The Problem-Solving Template

Apply this for every single problem before touching code:

```
1. UNDERSTAND   — Restate in your own words. What are the inputs/outputs? Constraints? Edge cases?
2. PATTERN MATCH — What category does this look like? (see patterns below)
3. BRUTE FORCE  — Describe the naive solution out loud. O(n²) is fine as a starting point.
4. OPTIMIZE     — What's the bottleneck? Would a hash map / two pointers / monotonic stack remove it?
5. CODE         — Only write code once you know the approach.
6. TEST         — Walk through 2–3 examples by hand. Include an empty input and a single-element case.
```

## Pattern Cheat Sheet

| Pattern | When to use it |
|---------|---------------|
| Arrays + Hashing | Need O(1) lookup, frequency count, or deduplication |
| Two Pointers | Sorted array, find pair/triplet, in-place shrink from both ends |
| Sliding Window | Contiguous subarray/substring with a constraint (max/min/sum) |
| Binary Search | Sorted input, or "find minimum X such that condition holds" |
| Recursion | Problem can be broken into same smaller problem |
| Backtracking | Explore all combinations/permutations, prune dead ends |
| Trees (DFS/BFS) | Hierarchical data, path problems, level-by-level processing |
| Graphs | Nodes + edges, connectivity, shortest path, cycle detection |
| Dynamic Programming | Overlapping subproblems, optimal substructure — "how many ways / min cost" |

## Daily Session Ritual (45–60 min)

```
:00  Pick today's problem from problems.md
:00  Set a 20-min timer — think on paper, no coding yet
:20  Write your approach as comments in the editor first
:25  Code the solution
:40  Test by hand with 2–3 examples
:45  If not solved: look at hint (not solution), try again 10 min
:55  Read one top solution, compare to yours
:60  Log result in progress.md — one sentence on what you learned
```

**Rule:** Never look at a full solution before spending 20 min thinking. Hints are fine.

## Phase Progression

| Phase | Weeks | Focus |
|-------|-------|-------|
| 1 | 1 | Setup + mental model (framework + template) |
| 2 | 2–8 | Pattern-by-pattern — 6 problems per week |
| 3 | 9–12 | Blind practice — random problems, no category label |
| 4 | 13+ | Company-specific sets (NeetCode company tags on LC Premium) |

## Mindset Rules

- Slow and understood > fast and memorized
- Stuck for 20 min = normal, not failure
- The goal per session is one insight, not one solved problem
- Speed is a byproduct of pattern recognition — it comes automatically
