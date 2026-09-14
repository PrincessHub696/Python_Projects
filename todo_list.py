tasks = []

try:
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

while True:
    print("1. Добавить задачу.")
    print("2. Удалить задачу.")
    print("3. Показать все задачи.")
    print("4. Выйти.")

    choice = input("Выберите действие: ")

    if choice == "1" or choice == "Добавить задачу.":
        task = input("Что добавить? ")
        tasks.append(task)
        print("Успешно добавлено!")
        with open("todo.txt", "a") as file:
            file.write(task + "\n")


    elif choice == "2" or choice == "Удалить задачу.":
        task = input("Что удалить? ")
        if task in tasks:
            tasks.remove(task)
            print("Успешно удалено!")
        else:
            print("Такой задачи нет.")

    elif choice == "3" or choice == "Показать все задачи.":
        print("Ваши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

    elif choice == "4" or choice == "Выйти.":
        with open("todo.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("До свидания!")
        break

    else:
        print("Неверный ввод. Попробуйте снова.")