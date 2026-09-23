from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import datetime
import random

BOT_TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я твой первый бот.")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - Начать работу\n"
        "/help - Список команд\n"
        "/time - Текущее время\n"
        "/date - Текущая дата\n"
        "/roll - Игра в кубик\n"
        "/coin - Игра в монетку\n"
        "/joke - Шутка"
        )


@dp.message(Command("time"))
async def cmd_time(message: types.Message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await message.answer(f"⏰ Текущее время: {now}")

@dp.message(Command("date"))
async def cmd_date(message: types.Message):
    today = datetime.datetime.now().strftime("%d.%m.%Y")
    await message.answer(f"🗓️ Сегодня: {today}")

@dp.message(Command("roll"))
async def cmd_roll(message: types.Message):
    result = random.randint(1, 6)
    await message.answer(f"🎲 Вы бросили кубик: {result}")

@dp.message(Command("coin"))
async def cmd_coin(message: types.Message):
    result = random.choice(["Орёл", "Решка"])
    await message.answer(f"🪙 {result}")

@dp.message(Command("joke"))
async def cmd_joke(message: types.Message):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что OCT 31 == DEC 25.",
        "Есть 10 типов людей: те, кто понимает двоичную систему и те, кто нет.",
        "Программист - это машина для превращения кофе в код."
    ]
    await message.answer(random.choice(jokes))

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 