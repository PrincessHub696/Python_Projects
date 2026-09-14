import random

secret = random.randint(1, 100) #компьютер загадал число от 1 до 100 включительно

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    if guess == secret:
        print("Ты угадал!")
        break
    elif guess < secret:
        print("Загаданное число БОЛЬШЕ")
    else:
        print("Загаданное число МЕНЬШЕ")