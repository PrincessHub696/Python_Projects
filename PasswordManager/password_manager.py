from cryptography.fernet import Fernet
import json
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key):
    with open("key.key", "wb") as file:
        file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def load_passwords(key):
    if not os.path.exists("passwords.json"):
        return {}

    with open("passwords.json", "r") as file:
        encrypted = file.read()

    if not encrypted:
        return {}

    return json.loads(decrypt_data(encrypted, key))

def save_passwords(passwords, key):
    data = json.dumps(passwords)
    encrypted = encrypt_data(data, key)

    with open("passwords.json", "w") as file:
        file.write(encrypted)

def main():
    if not os.path.exists("key.key"):
        key = generate_key()
        save_key(key)
        print("Ключ создан!")
    else:
        key = load_key()

    passwords = load_passwords(key)

    while True:
        print("\n1. Добавить пароль")
        print("2. Показать пароли")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            site = input("Сайт: ")
            login = input("Логин: ")
            password = input("Пароль: ")
            passwords[site] = {"login": login, "password": password}
            save_passwords(passwords, key)
            print("Пароль сохранен!")

        elif choice == "2":
            if not passwords:
                print("Паролей нет.")
            else:
                for site, data in passwords.items():
                    print(f"\nСайт: {site}")
                    print(f" Логин: {data['login']}")
                    print(f" Пароль: {data['password']}")

        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
