def load_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Что добавить? ")
    tasks.append(task)
    print("Успешно добавлено!")

def remove_task(tasks):
    task = input("Что удалить? ")
    if task in tasks:
        tasks.remove(task)
        print("Успешно удалено.")
    else:
        print("Этой задачи нет в списке")

def show_tasks(tasks):
    print("Ваши задачи:")
    if not tasks:
        print("Список задач пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

tasks = load_tasks()

while True:

    print("1. Добавить задачу.")
    print("2. Удалить задачу.")
    print("3. Показать все задачи.")
    print("4. Выйти.")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        remove_task(tasks)

    elif choice == "3":
        show_tasks(tasks)

    elif choice == "4":
        save_tasks(tasks)
        print("До свидания!")
        break
    else:
        print("Неправильный ввод. Попробуйте снова.")