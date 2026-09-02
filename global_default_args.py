# Глобальная переменная
counter = 0

def increment():
    global counter
    counter += 1
    print(counter)


increment()

# Параметры по умолчанию
def greet_user(name="Гость"):
    print(f"Привет, {name}!")


greet_user("Анна")
greet_user()

# Ключевые аргументы
def show_info(name, age):
    print(f"{name}, {age} лет")


show_info("Анна", 20)
show_info(age=25, name="Светлана")