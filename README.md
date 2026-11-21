# Users CRUD API (FastAPI + Docker)

REST API для управления пользователями (`id`, `name`, `email`) с хранением данных в памяти, упакованный в Docker-контейнер.

## Быстрый запуск через Docker (рекомендуется)

Убедитесь, что у вас установлен Docker и Docker Compose, затем выполните:

```bash
docker compose up --build
```

Или без Docker Compose:

```bash
docker build -t fastapi-users-crud .
docker run -p 8000:8000 fastapi-users-crud
```

После запуска API и интерактивная документация Swagger UI будут доступны по адресу:  
`http://127.0.0`

## Локальный запуск без Docker

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS (для Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload
```

## Эндпоинты

| Метод | Путь | Описание | Статус при успехе |
| :--- | :--- | :--- | :--- |
| `POST` | `/users` | Создать пользователя | `201 Created` |
| `GET` | `/users` | Получить список всех пользователей | `200 OK` |
| `GET` | `/users/{user_id}` | Получить пользователя по ID | `200 OK` |
| `PUT` | `/users/{user_id}` | Полностью обновить данные пользователя | `200 OK` |
| `PATCH` | `/users/{user_id}` | Частично обновить данные пользователя | `200 OK` |
| `DELETE` | `/users/{user_id}` | Удалить пользователя | `204 No Content` |
