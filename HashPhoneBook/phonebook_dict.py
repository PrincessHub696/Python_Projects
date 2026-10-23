phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print(f"Контакт {name} добавлен!")

def find_contact(name):
    number = phonebook.get(name, "Не найден")
    print(f"{name}: {number}")

def delete_contact(name):
    if name in phonebook:
        number = phonebook.pop(name)
        print(f"Контакт {name} ({number}) удален!")
    else:
        print(f"Контакт {name} не найден.")

def show_all():
    if not phonebook:
        print("Телефонная книга пуста.")
        return

    print("\nВсе контакты:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

while True:
    print("\n1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        number = input("Номер: ")
        add_contact(name, number)

    elif choice == "2":
        name = input("Введите имя для поиска: ")
        find_contact(name)

    elif choice == "3":
        name = input("Введите имя для удаления: ")
        delete_contact(name)

    elif choice == "4":
        show_all()

    elif choice == "5":
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")