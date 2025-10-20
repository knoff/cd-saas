<!-- markdownlint-configure-file {"MD041": false} -->

## [2025-10-16 13:03 GMT+3]

### chore: directory structure and base config

Создана структура проекта `cd-saas`, включающая `backend/` (FastAPI) и `frontend/` (React + Vite).
Добавлены базовые конфигурации `.gitignore`, `.pre-commit-config.yaml`, `pyproject.toml`, шаблоны для backend и frontend.
Реализованы минимальные модули: `app/main.py`, `app/api/health.py`, `app/core/config.py`, тест `tests/test_health.py`.
Подготовлен `frontend/index.html` и конфигурация Vite, сборка в `backend/app/static/web/`.

---

## [2025-10-16 13:47 GMT+3]

### docs: Определение структуры документации

Созданы файлы документации:
`README.md`, `CONTRIBUTING.md`, `docs/architecture.md`, `docs/README.md`.
Определены правила ветвления, формат коммитов, стандарты линтинга (`ruff`, `black`, `prettier`, `markdownlint`).
Добавлена диаграмма взаимодействия компонентов (Headunit ↔ ESP ↔ SaaS).

---

## [2025-10-20 11:55 GMT+3]

### docs(repo_instructions): AI workflow and repo_notes

Добавлены файлы `.repo_instructions/WORKFLOW.md` и `repo_notes.md`.
Определён процесс взаимодействия с ассистентом (этапы сессии, шаблоны для коммитов, сессий, задач).
Добавлены шаблоны `commit_template.md`, `session_log_template.md`, `task_comment_template.md`, `detour_template.md`.
Зафиксированы правила ведения репозиторных заметок и структура архитектурных описаний (`Общая роль`, `Функции SaaS`, `Архитектура frontend/backend`).
