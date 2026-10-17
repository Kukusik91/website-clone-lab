"""Install native agent templates without replacing existing configuration."""

from pathlib import Path
import argparse
import shutil


def install(host: str) -> list[Path]:
    skill = Path(__file__).resolve().parents[1]
    if skill.name != "dev-agent-workflow" or skill.parent.name != "skills" or skill.parent.parent.name != ".agents":
        raise ValueError("Install the skill at <project>/.agents/skills/dev-agent-workflow first")
    target = skill.parent.parent.parent
    source = skill / "templates" / host / "agents"
    destination = target / f".{host}" / "agents"
    files = list(source.iterdir())
    conflicts = [destination / file.name for file in files if (destination / file.name).exists()]
    if conflicts:
        raise FileExistsError("Existing agents; merge manually: " + ", ".join(map(str, conflicts)))
    destination.mkdir(parents=True, exist_ok=True)
    for file in files:
        shutil.copy2(file, destination / file.name)
    return [destination / file.name for file in files]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host", choices=("codex", "cursor"))
    args = parser.parse_args()
    for path in install(args.host):
        print(path)
