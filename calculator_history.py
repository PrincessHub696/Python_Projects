def calc(a, b, op):

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b != 0:
            result = a / b
        else:
            print("Делить на ноль нельзя!")
            return
    else:
        print("Неверная операция")
        return
    
    print(f"Результат: {result}")

    # Запись в файл
    with open("history_calculator.txt", "a") as file:
        file.write(f"{a} {op} {b} = {result}\n")

def show_history():
    try:
        with open("history_calculator.txt", "r") as file:
            content = file.readlines()
            if content:
                print("Последние 5 операций:")
                for line in content[-5:]:
                    print(line.strip())
            else:
                print("История пуста.")
    except FileNotFoundError:
        print("История пока пуста.")

while True:

    print("\n1. Калькулятор")
    print("2. История вычислений")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1" or choice == "Калькулятор":
        a = int(input("Введите первое число: "))
        op = input("Введите знак операции(+, -, *, /): ")
        b = int(input("Введите второе число: "))
        calc(a, b, op)

    elif choice == "2" or choice == "История вычислений" or choice == "История":
        show_history()

    elif choice == "3" or choice == "Выход":
        print("До свидания!")
        break

    else:
        print("Неверный выбор, попробуйте снова.")