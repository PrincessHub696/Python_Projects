a = input("Введите числа через пробел: ")
numbers = a.split()
int_numbers = []    # Пустой список

for item in numbers:
    num = int(item)    # Превращает строку в число
    int_numbers.append(num)

int_numbers = set(int_numbers)    # Превращаем список во множество
print(int_numbers)    # Выводим множество