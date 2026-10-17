$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$skillRoot = Join-Path $root '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null

$workflow = Join-Path $skillRoot 'dev-agent-workflow'
if (-not (Test-Path (Join-Path $workflow 'SKILL.md'))) {
    git clone https://github.com/Evgen-rus/dev-agent-workflow.git $workflow
}
python (Join-Path $workflow 'scripts/install.py') codex

if (-not (Get-Command pnpm -ErrorAction SilentlyContinue)) {
    throw 'pnpm is required. Install Node.js and pnpm, then rerun this script.'
}
pnpm dlx impeccable install --providers=codex --scope=project
