# Weather Bot

Telegram-бот, который показывает погоду в сохраненном городе.

## Фунционал

- `/start` - приветствие
- `/setcity Москва` - установить город
- `/weather` - показать погоду в сохраненном городе

## Как запустить

1. Установи Python 3.
2. Установи зависимости:

```
pip install aiogram requests
```

3. Получи токен у `@BotFather` в Telegram.
4. Получи API-ключ на `openweathermap.org`.
5. Вставь токен и ключ в файл `weather_bot.py`.
6. Запусти бота:

```
python weather_bot.py
```

7. В Telegram:
    - `/setcity Москва`
    - `/weather`

## Технологии

- Python 3
- Библиотека `aiogram`
- Библиотека `requests`
- База данных SQLite (`sqlite3`)

## Автор

PrincessHub696