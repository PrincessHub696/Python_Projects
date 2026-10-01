## Reminder Bot

Telegram-бот для напоминаний

## Функционал

- `/start` - приветствие
- `/remind Текст напоминания : 30` - напомнить через 30 минут
- Отправляет напоминание в чат

## Как запустить

1. Установи Python 3.
2. Установи библиотеку `aiogram`:

```
pip install aiogram
```

3. Получи токен у `@BotFather` в Telegram.
4. Вставь токен в файл `reminder_bot.py`.
5. Запусти бота:

```
python reminder_bot.py
```

6. В Telegram:
    - `/start`
    - `/remind Позвонить маме : 30`

## Технологии

- Python 3
- Библиотека `aiogram`
- Модуль `asyncio` (для отложенных задач)
- Модуль `datetime`

## Автор

PrincessHub696