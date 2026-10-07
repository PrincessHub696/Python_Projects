import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        group_name TEXT
    )
""")
conn.commit()

def add_student(name, age, group_name):
    cursor.execute("""
        INSERT INTO students (name, age, group_name)
        VALUES (?, ?, ?)
    """, (name, age, group_name))
    conn.commit()
    print(f"Студент {name} добавлен!")

def show_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("Студентов нет.")
        return

    print("\nСписок студентов:")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}, Группа: {row[3]}")

def find_student(name):
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    row = cursor.fetchone()

    if row:
        print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}, Группа: {row[3]}")
    else:
        print(f"Студент {name} не найден.")

def update_student(name, new_age):
    cursor.execute("UPDATE students SET age = ? WHERE name = ?", (new_age, name))
    conn.commit()
    print(f"Возраст студента {name} обновлен!")

def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    row = cursor.fetchone()

    if row:
        cursor.execute("DELETE FROM students WHERE name = ?", (name,))
        conn.commit()
        print(f"Студент {name} удален!")
    else:
        print(f"Студент {name} не найден.")

while True:
    print("\n1. Добавить студента")
    print("2. Показать всех студентов")
    print("3. Найти студента")
    print("4. Обновить возраст")
    print("5. Удалить студента")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        age = int(input("Возраст: "))
        group_name = input("Группа: ")
        add_student(name, age, group_name)

    elif choice == "2":
        show_students()

    elif choice == "3":
        name = input("Введите имя: ")
        find_student(name)

    elif choice == "4":
        name = input("Введите имя: ")
        new_age = int(input("Новый возраст: "))
        update_student(name, new_age)

    elif choice == "5":
        name = input("Введите имя: ")
        delete_student(name)

    elif choice == "6":
        conn.close()
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")