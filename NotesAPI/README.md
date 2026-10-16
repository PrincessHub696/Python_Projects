# Notes API

REST API для заметок на Flask.

## Функционал

- Получение всех заметок (GET)
- Добавление заметок (POST)
- Удаление заметки по ID (DELETE)

## Как запустить

1. Установи Python 3.
2. Установи Flask:

```
pip install flask
```

3. Запусти:

```
python app.py
```

4. API доступно по адресу: http://127.0.0.1:5000/

## Эндпоинты

| Метод | URL | Что делает |
| :--- | :--- | :--- |
| GET | `/api/notes` | Получить все заметки |
| POST | `/api/notes` | Добавить заметку |
| DELETE | `/api/notes/<id>` | Удалить заметку |

## Пример запроса (POST)

```python
import requests

requests.post("http://127.0.0.1:5000/api/notes", json={
    "title": "Заметка",
    "text": "Привет"
})
```

## Технологии

- Python 3
- Flask
- REST API
- JSON

## Автор

PrincessHub696