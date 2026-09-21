import random

words = ["питон", "яблоко", "призма", "компьютер", "алгоритм", "словарь", "синтаксис", "программа", "функция", "переменная"]
secret_word = random.choice(words)

mask = []
for letter in secret_word:
    mask.append("_")

attempts = 6

while True:
    print(" ".join(mask))
    guess = input("Введите букву: ").lower()

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                mask[i] = guess

    else:
        attempts -= 1
        print(f"Неверно. Осталось попыток: {attempts}")

    if "_" not in mask:
        print("Поздравляю! Вы угадали слово!")
        break

    if attempts == 0:
        print(f"Вы проиграли. Было загадано слово: {secret_word}")
        break
    