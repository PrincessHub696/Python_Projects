import random

def roll_dice():
    result = random.randint(1, 6)
    return result

while True:
    player = roll_dice()
    computer = roll_dice()

    print(f"Вы бросили: {player}")
    print(f"Компьютер бросил: {computer}")

    if player > computer:
        print("Вы победили!")
    elif player < computer:
        print("Компьютер победил!")
    else:
        print("Ничья!")

    again = input("Хотите сыграть еще раз? (да/нет) ").lower()
    if again != "да":
        print("До свидания!")
        break