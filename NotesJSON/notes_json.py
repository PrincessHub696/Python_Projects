import json

notes = []

def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def add_note(notes):
    title = input("Введите заголовок: ")
    text = input("Введите текст заметки: ")
    notes.append({"title": title, "text": text})
    print("Заметка добавлена!")

def show_notes(notes):
    if not notes:
        print("Заметок нет.")
        return

    print("Ваши заметки:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}")
        print(f"    {note['text']}")

notes = load_notes()

while True:
    print("\n1. Добавить заметку.")
    print("2. Показать все заметки.")
    print("3. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_note(notes)
        save_notes(notes)

    elif choice == "2":
        show_notes(notes)

    elif choice == "3":
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")


