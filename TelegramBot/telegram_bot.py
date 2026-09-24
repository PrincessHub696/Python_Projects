from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import datetime
import random
import requests

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
        "/menu - Показать кнопки\n"
        "/start - Начать работу\n"
        "/help - Список команд\n"
        "/time - Текущее время\n"
        "/date - Текущая дата\n"
        "/roll - Игра в кубик\n"
        "/coin - Игра в монетку\n"
        "/weather - Погода\n"
        "/joke - Шутка"
        )

@dp.message(Command("menu"))
async def cmd_menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard =[
            [KeyboardButton(text="⏰ Текущее время"), KeyboardButton(text="🗓️ Текущая дата")],
            [KeyboardButton(text="🎲 Игра в кубик"), KeyboardButton(text="🪙 Игра в монетку")],
            [KeyboardButton(text="🤡 Шутка"), KeyboardButton(text="🌤️ Погода")]
        ],
        resize_keyboard=True
    )
    await message.answer("Выбери команду:", reply_markup=keyboard)

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

WEATHER_API_KEY = "ТВОЙ_КЛЮЧ_ЗДЕСЬ"

@dp.message(Command("weather"))
async def cmd_weather(message: types.Message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.answer("Напиши: /weather Москва")
        return

    city = args[1]
    ur1 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(ur1)
        data = response.json()

        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            await message.answer(f"🌤️ В городе {city}: {temp}°C, {desc}")
        else:
            await message.answer("Город не найден. Попробуй другой.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

@dp.message(lambda message: message.text == "⏰ Текущее время")
async def btn_time(message: types.Message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await message.answer(f"⏰ Текущее время: {now}")

@dp.message(lambda message: message.text == "🗓️ Текущая дата")
async def btn_date(message: types.Message):
    today = datetime.datetime.now().strftime("%d.%m.%Y")
    await message.answer(f"🗓️ Сегодня: {today}")

@dp.message(lambda message: message.text == "🎲 Игра в кубик")
async def btn_roll(message: types.Message):
    result = random.randint(1, 6)
    await message.answer(f"🎲 Вы бросили кубик: {result}")

@dp.message(lambda message: message.text == "🪙 Игра в монетку")
async def btn_coin(message: types.Message):
    result = random.choice(["Орёл", "Решка"])
    await message.answer(f"🪙 {result}")

@dp.message(lambda message: message.text == "🤡 Шутка")
async def btn_joke(message: types.Message):
    jokes = [
            "Почему программисты путают Хэллоуин и Рождество? Потому что OCT 31 == DEC 25.",
            "Есть 10 типов людей: те, кто понимает двоичную систему и те, кто нет.",
            "Программист - это машина для превращения кофе в код."
        ]
    await message.answer(random.choice(jokes))

@dp.message(lambda message: message.text == "🌤️ Погода")
async def btn_weather(message: types.Message):
    await message.answer("Напиши название города, например: Москва")

@dp.message(lambda message: message.text and not message.text.startswith("/") and len(message.text.split()) <= 3)
async def get_city(message: types.Message):
    city = message.text
    ur1 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    
    try:
        response = requests.get(ur1)
        data = response.json()
    
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            await message.answer(f"🌤️ В городе {city}: {temp}°C, {desc}")
        else:
            await message.answer("Город не найден. Попробуй другой.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 