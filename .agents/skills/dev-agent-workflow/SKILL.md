---
name: dev-agent-workflow
description: Coordinate Codex or Cursor subagents for repository development with bounded context, clear ownership, concise handoffs, and integrated verification. Use for substantial coding tasks that may benefit from delegation; skip for trivial edits and non-development requests.
---

# Development through agents

Aim to minimize the total cost of a reliably finished task: investigation, agent work, coordination, fixes, and verification. Do not optimize one agent's token count at the expense of correctness or extra work elsewhere.

## Understand the repository

1. Read the user's request and applicable repository instructions. Check the working tree before edits; preserve unrelated changes.
2. Find the relevant architecture map or documentation if it exists. Read only the needed sections, source ranges, callers, and tests. Source code and configuration settle conflicts with documentation.
3. Keep project-specific contracts, commands, model availability, and permissions in the project. Do not assume any particular language, framework, or file layout.

## Choose who works

- The current agent remains primary: it owns the task, architecture and contract decisions, integration, and final acceptance. Do not create a second lead agent.
- Handle a small, known change directly when delegation would cost more than the work.
- Use `code-mapper` (or the host's read-only scout) for broad codebase mapping, unfamiliar modules, large files, symbols, callers/callees, call chains, or related tests. Roughly 600 lines is a cue, not a threshold. Ask for exact paths and relevant ranges. After its report, read only the original ranges that determine a consequential change.
- Delegate bounded implementation to `worker-low` for routine work or `worker-xhigh` for complex local work when the handoff is worthwhile. Use native Codex or Cursor agents and project or host model routing. If a requested model is unavailable, use only a host-supported fallback and disclose the change; never silently substitute a model. Keep model IDs out of this skill.
- Usually run at most two workers at once. Add a third only for a large task with an independent workstream and a real time or context benefit. Give each changed file one writer. Do not ask workers to delegate again.
- Count a read-only scout separately from implementation workers. Do not run duplicate scouts over the same area.

## Give and receive narrow context

Give a worker the goal, owned files or symbols, relevant repository rules, constraints, expected result, and checks. Prefer fresh context when supported; pass prior conversation only when needed. Exclude secrets and private data.

Request a short handoff:

    FINDINGS: decision-relevant facts with path:line references
    CHANGES: what changed, or none
    FILES: files touched
    RISKS: unresolved issues, or none
    VERIFICATION: commands, results, checked revision, and justified skips

Do not forward chain-of-thought, full transcripts, long successful test logs, or unrelated search results. If the next useful step depends on a worker, wait for its handoff instead of duplicating its investigation. Work in parallel only on independent tasks.

For a scout, request `FINDINGS / RELEVANT_RANGES / CALLERS / CALLEES / TESTS / RISKS` with concise path:line evidence.

## Integrate and verify

Primary reviews the final diff, ownership boundaries, and cross-layer contracts. Personally inspect decisive source ranges for security, authorization, concurrency, migrations, data integrity, and complex state changes. Run targeted checks first; run the project's required integrated checks once on the combined result. Reuse a passing check only when its inputs have not changed. Never cut essential validation to save tokens.

After implementation, primary decides whether independent `verifier` review adds value. Usually use it for UI/UX, API/runtime, deploy/config/integration, or critical business logic, complex state, concurrency, auth, and migrations. Usually skip it for docs, mechanical edits, or a small backend fix covered by good targeted tests. Give it the user/system contract and changed scenario; it checks independently and does not own architecture or final acceptance. On FAIL, fix and reverify the affected contract; on BLOCKED, report the missing check. Do not invoke it after every edit.

Report what changed, which contract was checked, the verification result, and any explicit limitations. This skill does not authorize paid calls, production changes, publishing, external messages, or edits outside the user's requested scope.
