grade = int(input("Введите оценку (от 1 до 5): "))

if grade == 5:
    print("Отлично!")
elif grade == 4:
    print("Хорошо!")
elif grade == 3:
    print("Удовлетворительно!")
elif grade == 2 or grade == 1:
    print("Плохо!")
else:
    print("Некорректная оценка! Введите число от 1 до 5.")