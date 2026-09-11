import random

def get_secret():
    return random.randint(1, 100)

def get_sucessful(secret, guess):
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        return True

def play_game():
    secret = get_secret()
    while True:
        guess = int(input("Угадай число от 1 до 100: "))
        if get_sucessful(secret, guess):
            print("Поздравляю! Вы угадали!")
            break

play_game()