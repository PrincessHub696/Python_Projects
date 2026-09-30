import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import requests

BOT_TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"
WEATHER_API_KEY = "ТВОЙ_КЛЮЧ_ЗДЕСЬ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Подключаемся к базе
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Создаем таблицу с id пользователя, городом и сохранением
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        city TEXT
    )
""")
conn.commit()

# Замена города, если пользователь уже есть, плейсхолдеры для безопасности (защита от SQL-инъекций)
def set_city(user_id, city):
    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, city)
        VALUES (?, ?)
    """, (user_id, city))
    conn.commit()

# Поиск города по id пользователя
def get_city(user_id):
    cursor.execute("SELECT city FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот погоды.\n"
        "Сначала установи город: /setcity Москва\n"
        "Потом узнай погоду: /weather"
    )

@dp.message(Command("setcity"))
async def cmd_setcity(message: types.Message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.answer("Напиши: /setcity Москва")
        return

    city = args[1]
    set_city(message.from_user.id, city)
    await message.answer(f"Город сохранен: {city}")

@dp.message(Command("weather"))
async def cmd_weather(message: types.Message):
    user_id = message.from_user.id
    city = get_city(user_id)

    if not city:
        await message.answer("Сначала установи город: /setcity Москва")
        return

    ur1 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(ur1)
        data = response.json()

        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            await message.answer(f"🌤️ В городе {city}: {temp}°C, {desc}")
        else:
            await message.answer("Город не найден. Проверь название.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())