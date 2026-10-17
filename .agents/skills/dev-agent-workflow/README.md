# dev-agent-workflow

A portable skill with native Codex and Cursor subagent templates. The user-selected model remains primary; the skill never creates another lead.

[Русская инструкция](README.ru.md)

## Install in a project

Once the files are published, create `.agents/skills/` in the target project's root and clone [this repository](https://github.com/Evgen-rus/dev-agent-workflow) into it:

    git clone https://github.com/Evgen-rus/dev-agent-workflow.git .agents/skills/dev-agent-workflow

Then install the host-specific agents from the cloned folder:

    python .agents/skills/dev-agent-workflow/scripts/install.py codex
    python .agents/skills/dev-agent-workflow/scripts/install.py cursor

The installer derives the project root from the skill's location and copies four files only into that project's `.codex/agents/` or `.cursor/agents/`. It stops before writing if a matching agent exists. Compare and merge that file manually. It never edits `AGENTS.md`, Cursor rules, or Codex `config.toml`. Restart the host if needed. Cloning the skill alone does not activate native agents.

| Role | Codex default | Cursor default |
| --- | --- | --- |
| `worker-low` | GPT-6 Luna, low | Inherit primary |
| `worker-xhigh` | GPT-6 Luna, xhigh | Inherit primary |
| `code-mapper` | GPT-6 Luna, medium; read-only sandbox | Inherit primary; `readonly: true` |
| `verifier` | GPT-6 Luna, xhigh | Inherit primary |

Model IDs live in `templates/codex/agents/*.toml`, not in `SKILL.md`. For a project override, edit the installed `.codex/agents/worker-xhigh.toml`, keeping its required fields, and set `model = "gpt-6-sol"` and `model_reasoning_effort = "high"`. For Cursor, edit the installed `.cursor/agents/worker-xhigh.md` frontmatter, replacing `model: inherit` with an available model ID. If Luna is unavailable, explicitly choose an available model or use a host-supported fallback and disclose the substitution. Cursor may apply its own compatible fallback under plan or admin restrictions; check the actual model.

Invoke it explicitly as `$dev-agent-workflow` in Codex, or ask either agent to use the development-agent workflow when planning substantial repository work. Automatic selection is also available when the task matches the skill description.

Small known edits stay with primary. Broad investigation goes to `code-mapper`, then primary reads decisive source ranges. Routine implementation goes to `worker-low`; complex bounded work to `worker-xhigh`. Primary calls `verifier` when independent contract checking is useful, then owns final acceptance. Project instructions remain authoritative. Cursor remote/cloud agents may need the project-level copy.

Licensed under MIT. See [LICENSE](LICENSE).
