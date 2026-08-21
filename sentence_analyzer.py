sentence = input("Введите предложение: ")

words = sentence.split() #разбиваем на слова

#1.Количество слов:
print("Количество слов: ", len(words))

#2.Самое длинное слов:
longest = max(words, key=len)
print("Самое длинное слово: ", longest)

#3.Перевернуть все предложение:
print("Все предложение наоборот: ", sentence[::-1])

#4.Перевернуть каждое слово:
reserved_words = [word[::-1] for word in words]
print("Слова задом наперед: ", reserved_words)

#5.Склеить обратно через пробел:
print("Склеили обратно через пробел: ", " ".join(words))