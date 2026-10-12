import sqlite3
import datetime

conn = sqlite3.connect("blog.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        date TEXT
    )
""")
conn.commit()

def add_post(title, content):
    date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    cursor.execute("""
        INSERT INTO posts (title, content, date)
        VALUES (?, ?, ?)
    """, (title, content, date))
    conn.commit()
    print(f"Пост <<{title}>> добавлен!")

def show_posts():
    cursor.execute("SELECT * FROM posts ORDER BY id DESC")
    rows = cursor.fetchall()

    if not rows:
        print("Постов нет.")
        return

    print("\nВсе посты:")
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"Заголовок: {row[1]}")
        print(f"Дата: {row[3]}")
        print(f"Текст: {row[2]}")
        print("-" * 30)

def delete_post(post_id):
    cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    row = cursor.fetchone()

    if row:
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        print(f"Пост с ID {post_id} удален!")

    else:
        print(f"Пост с ID {post_id} не найден.")

while True:
    print("\n1. Добавить пост")
    print("2. Показать все посты")
    print("3. Удалить пост")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Заголовок: ")
        content = input("Текст: ")
        add_post(title, content)

    elif choice == "2":
        show_posts()

    elif choice == "3":
        post_id = int(input("ID поста для удаления: "))
        delete_post(post_id)

    elif choice == "4":
        conn.close()
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")