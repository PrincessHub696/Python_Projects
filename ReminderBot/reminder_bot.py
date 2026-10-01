from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import datetime

BOT_TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот-напоминалка.\n"
        "Напиши: /remind Текст напоминания : 30\n"
        "Где 30 - через сколько минут напомнить."
    )

@dp.message(Command("remind"))
async def cmd_remind(message: types.Message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.answer("Напиши: /remind Текст напоминания : 30")
        return

    text = args[1]

    # Разбиваем на текст и время
    parts = text.rsplit(":", 1)

    if len(parts) < 2:
        await message.answer("Напиши: /remind Текст напоминания : 30")
        return
    
    reminder_text = parts[0].strip()
    try:
        minutes = int(parts[1].strip())
    except ValueError:
        await message.answer("Время должно быть числом (в минутах).")
        return

    await message.answer(f"Ок! Напомню через {minutes} минут: <<{reminder_text}>>")

    await asyncio.sleep(minutes * 60)    # Ждем minutes минут

    await message.answer(f"Напоминание: {reminder_text}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())