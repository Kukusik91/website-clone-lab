# dev-agent-workflow

Переносимый скилл с нативными шаблонами субагентов Codex и Cursor. Primary остаётся моделью, выбранной пользователем; второго lead скилл не создаёт.

[English instructions](README.md)

## Установка в проект

После публикации файлов создайте в корне нужного проекта каталог `.agents/skills/` и клонируйте туда [этот репозиторий](https://github.com/Evgen-rus/dev-agent-workflow):

    git clone https://github.com/Evgen-rus/dev-agent-workflow.git .agents/skills/dev-agent-workflow

Затем установите агентов нужного хоста из клона:

    python .agents/skills/dev-agent-workflow/scripts/install.py codex
    python .agents/skills/dev-agent-workflow/scripts/install.py cursor

Скрипт определяет корень проекта по расположению скилла и копирует четыре файла только в `.codex/agents/` или `.cursor/agents/` этого проекта. Если агент с тем же именем уже существует, скрипт прекращает работу до записи. Сравните и объедините такой файл вручную. `AGENTS.md`, правила Cursor и `config.toml` Codex не меняются. Если агенты не появились, перезапустите хост. Одно лишь клонирование скилла не активирует нативных агентов.

| Роль | Codex по умолчанию | Cursor по умолчанию |
| --- | --- | --- |
| `worker-low` | GPT-6 Luna, low | Наследует primary |
| `worker-xhigh` | GPT-6 Luna, xhigh | Наследует primary |
| `code-mapper` | GPT-6 Luna, medium; read-only sandbox | Наследует primary; `readonly: true` |
| `verifier` | GPT-6 Luna, xhigh | Наследует primary |

ID моделей находятся в `templates/codex/agents/*.toml`, не в `SKILL.md`. Для проектного override измените установленный `.codex/agents/worker-xhigh.toml`, сохранив обязательные поля: `model = "gpt-6-sol"`, `model_reasoning_effort = "high"`. В Cursor замените `model: inherit` на доступный ID в `.cursor/agents/worker-xhigh.md`. Если Luna недоступна, явно выберите доступную модель или примените поддерживаемый хостом fallback и сообщите о замене. Cursor может сам выбрать совместимую модель при ограничении тарифа или администратора; проверьте фактическую модель.

В Codex его можно вызвать явно как `$dev-agent-workflow`. В Codex или Cursor можно также попросить агента применить процесс разработки через субагентов к объёмной задаче. При подходящем описании задачи скилл может выбираться автоматически.

Малую известную правку primary делает сам. Широкое исследование идёт в `code-mapper`, затем primary читает критические исходные ranges. Рутинная реализация идёт в `worker-low`, сложная bounded-реализация — в `worker-xhigh`. Primary вызывает `verifier`, когда полезна независимая проверка контракта, и сам принимает итог. Проектные инструкции остаются главными. Для удалённых агентов Cursor может понадобиться проектная копия скилла.

Лицензия MIT: см. [LICENSE](LICENSE).
