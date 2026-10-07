questions = [
    {
        "question": "Столица России?",
        "options": ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"],
        "answer": "Москва"
    },
    {
        "question": "Сколько будет 5 + 3?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Сколько дней в неделе?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Сколько часов в сутках?",
        "options": ["24", "12", "20", "6"],
        "answer": "24"
    },
    {
        "question": "Кто написал 'Войну и мир'?",
        "options": ["Пушкин", "Толстой", "Достоевский", "Чехов"],
        "answer": "Толстой"
    }
]

score = 0

for i, q in enumerate(questions, 1):
    print(f"\nВопрос {i}: {q['question']}")

    for j, option in enumerate(q["options"], 1):
        print(f" {j}. {option}")

    answer = input("Ваш ответ (номер): ")

    if q["options"][int(answer) - 1] == q["answer"]:
        print("Правильно!")
        score += 1

    else:
        print(f"Неправильно. Правильный ответ: {q['answer']}")

print(f"\nВаш результат: {score} из {len(questions)}")