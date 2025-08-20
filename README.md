# Task Manager — Тестовое задание

**Стек:**

* Python 3.12+
* FastAPI 
* asyncpg (Postgres driver)
* Gunicorn + Uvicorn workers
* Docker + docker-compose
* Ruff + mypy для проверки статики и качества кода
* Uv в качестве менеджера пакетов
* pre-commit для хуков

---

## Быстрый старт

```bash
git clone https://github.com/netstrrex/TaskManagerCRUD.git
cd TaskManagerCRUD
```

Создайте .env файл в корне проекта

### Запуск приложения через Docker

```bash
docker compose up --build -d
```

### Запуск приложения локально

 ```bash
 uv sync
 pre-commit install
 python /src/main.py
 ```
---

## API — эндпоинты

> Базовый префикс: `/api/v1/task`

* `POST /api/v1/task` — создать задачу.
* `GET /api/v1/task/?uuid={id}` — получить задачу по UUID.
* `GET /api/v1/task/all` — получить список задач.
* `PUT /api/v1/task` — обновление задачи.
* `DELETE /api/v1/task/?uuid={id}` — удаление задачи.

Полная документация swagger: `/docs` 
