import random
import string

characters = string.ascii_letters + string.digits + string.punctuation  # Создаем строку из букв, символов и цифр
lenght = int(input("Введите длину пароля: "))

password = ""
for _ in range(lenght):
    password += random.choice(characters)

print(f"Ваш пароль: {password}")