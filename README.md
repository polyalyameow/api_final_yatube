## API для платформы Yatube

Yatube - социальная сеть, в которой можно публиковать и комментировать посты,
подписываться на интересных авторов и искать записи по интресам. Для публикации
и комментирования постов необходима регистрация.

### Технологии

Python
Django
Django REST Framework
SQLite3

### Запуск проекта

Создаем виртуальное окружение:

```
python -m venv venv
```

Активируем виртуальное окружение:

```
venv\Scripts\activate
```

Устанавливаем зависимости

```
pip install -r requirements.txt
```

Выполняем миграции

```
python3 manage.py migrate
```

Запускаем проект

```
python3 manage.py runserver
```

### Примеры запросов

`GET: api/v1/posts/{id}/`

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

`POST: api/v1/posts/`

Отправляем:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Получаем:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

`PUT: api/v1/posts/{id}/`

Отправляем:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Получаем:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
