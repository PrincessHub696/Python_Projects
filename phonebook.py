phonebook = {}    # Пустой словарь

print("Телефонная книга:")

while True:
    print("1. Добавить номер телефона")
    print("2. Удалить номер телефона")
    print("3. Найти номер по имени")
    print("4. Показать все контакты")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя: ")

        if name in phonebook:
            answer = input("Такой контакт уже есть. Хотите обновить?(да|нет): ")

            if answer == "да":
                new_number = input("Введите новый номер: ")
                phonebook[name] = new_number
                print("Номер обновлён!")
            else:
                print("Обновление отменено.")

        else:
            number = input("Введите номер: ")
            phonebook[name] = number
            print("Контакт добавлен!")

    elif choice == "2":
        answer1 = input("Какой контакт вы хотите удалить? ")

        if answer1 in phonebook:
            del phonebook[answer1]
            print("Контакт успешно удален!")
        else:
            print("Проверьте правильность ввода имени или контакта нет в телефонной книге.")

    elif choice == "3":
        name1 = input("Введите имя контакта: ")

        if name1 in phonebook:
            print(f"{name1}: {phonebook[name1]}")
        else:
            print("Проверьте правильность ввода имени или контакта нет в телефонной книге.")

    elif choice == "4":
        print("Ваши контакты:")
        for index, item in enumerate(phonebook, 1):
            print(f"{index}. {item}")
        print()

    elif choice == "5":
        print("Успешный выход!")
        break
    else:
        print("Неверный выбор, попробуйте снова.")