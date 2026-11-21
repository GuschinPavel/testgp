# Users CRUD API (FastAPI + Docker)

REST API для управления пользователями (`id`, `name`, `email`) с хранением данных в памяти, упакованный в Docker-контейнер.

## Быстрый запуск через Docker (рекомендуется)

Убедитесь, что у вас установлен Docker и Docker Compose, затем выполните:

git clone https://github.com/GuschinPavel/testgp
cd testgp
docker compose up -d

После запуска API и интерактивная документация Swagger UI будут доступны по адресу:  
`http://127.0.0.1:8000/docs


## Эндпоинты

| Метод | Путь | Описание | Статус при успехе |
| :--- | :--- | :--- | :--- |
| `POST` | `/users` | Создать пользователя | `201 Created` |
| `GET` | `/users` | Получить список всех пользователей | `200 OK` |
| `GET` | `/users/{user_id}` | Получить пользователя по ID | `200 OK` |
| `PUT` | `/users/{user_id}` | Полностью обновить данные пользователя | `200 OK` |
| `PATCH` | `/users/{user_id}` | Частично обновить данные пользователя | `200 OK` |
| `DELETE` | `/users/{user_id}` | Удалить пользователя | `204 No Content` |
