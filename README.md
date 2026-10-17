# Website Clone Lab

A minimal starter for website cloning experiments: FastAPI backend and Vite frontend, with project-local Codex skills.

## Requirements

- Python 3.10+
- Node.js 20+ and pnpm
- Git

## Setup

Clone the project, then install the project-local Codex skills and dependencies:

```powershell
git clone https://github.com/Kukusik91/website-clone-lab.git
cd website-clone-lab
powershell -ExecutionPolicy Bypass -File scripts/install-skills.ps1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend/requirements.txt
pnpm --dir frontend install
```

The skill installer checks out the latest upstream `dev-agent-workflow` and Impeccable sources into the project, then installs their Codex-specific project files. Because upstream skills change, rerun the installer to refresh them. Restart Codex or reopen the project if a newly installed skill does not appear. In Codex, approve Impeccable's project hook if prompted. Start Impeccable once with `$impeccable init` to create project design context.

## Run

In one PowerShell terminal:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn main:app --app-dir backend --reload
```

In another PowerShell terminal:

```powershell
pnpm --dir frontend dev
```

The API is at <http://127.0.0.1:8000> and the frontend at <http://localhost:5173>.

## Build frontend

```powershell
pnpm --dir frontend build
```

## Codex skills

- `$dev-agent-workflow` provides the repository development workflow. Its Codex installer creates native agents under `.codex/agents/`.
- `$impeccable` provides design guidance and commands; its Codex installer also adds the project hook under `.codex/hooks.json`.
- Both skill source checkouts and generated Codex configuration are project-local and committed, so they are available after cloning. The installer does not overwrite existing Codex agent files.

