shopping_list = [] #пустой список

print("Список покупок:")

while True:
    print("1. Добавить товар")
    print("2. Удалить товар")
    print("3. Показать список")
    print("4. Очистить список")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        shopping_list.append(input("Что добавить? "))
        print("Товар добавлен!")
    elif choice == "2":
        item = input("Что удалить? ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Товар удален!")
        else:
            print("Такого товара нет в списке.")
    elif choice == "3":
        print("Ваш список покупок: ")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
        print()
    elif choice == "4":
        shopping_list.clear()
        print("Список очищен!")
    elif choice == "5":
        print("Успешный выход!")
        break
    else:
        print("Неверный выбор, попробуйте снова.")