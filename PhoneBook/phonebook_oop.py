class PhoneBook:
    def __init__(self):
        self.contacts = {}  # Пустой словарь для контактов

    def add_contact(self, name, number):  # Добавить контакт
        self.contacts[name] = number

    def find_contact(self, name):  # Найти контакт
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Контакт не найден или неправильно введен.")

    def delete_contact(self, name):  # Удалить контакт
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Контакт не найден или неправильно введен.")

    def show_all(self):  # Показать все
        if self.contacts:
            print("Контакты:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("Телефонная книга пуста.")

    def save_to_file(self):  # Сохранить в файл
        with open("phonebook.txt", "w") as file:
            for name, number in self.contacts.items():
                file.write(f"{name}:{number}\n")

    def load_from_file(self):  # Загружаем контакты из файла
        try:
            with open("phonebook.txt", "r") as file:
                self.contacts = {}
                for line in file.readlines():
                    parts = line.strip().split(":")  # Проверяем, что частей ровно 2
                    if len(parts) == 2:
                        name, number = parts
                        self.contacts[name] = number
        except FileNotFoundError:
            self.contacts = {}
            print("Телефонная книга еще пуста.")

book = PhoneBook()
book.load_from_file()

while True:
    print("1. Добавить контакт.")
    print("2. Удалить контакт.")
    print("3. Найти контакт.")
    print("4. Показать все контакты.")
    print("5. Сохранить файл.")
    print("6. Выйти.")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя: ")
        number = input("Введите номер: ")
        book.add_contact(name, number)

    elif choice == "2":
        name = input("Введите имя для удаления: ")
        book.delete_contact(name)
        print("Контакт успешно удален!")

    elif choice == "3":
        name = input("Введите имя для поиска: ")
        book.find_contact(name)

    elif choice == "4":
        book.show_all()

    elif choice == "5":
        book.save_to_file()
        print("Контакты сохранены в файл.")

    elif choice == "6":
        book.save_to_file()
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")