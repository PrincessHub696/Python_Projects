def analyze_text(text):
    words = len(text.split())
    letters = len(text.replace(" ", ""))
    return words, letters

text = input("Введите текст: ")
words, letters = analyze_text(text)
print(f"Количество слов: {words}")
print(f"Количество символов (без пробелов): {letters}")