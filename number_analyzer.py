analyzer_list = [] #Пустой список

for i in range(1,6):
    analyzer_list.append(int(input("Введите число: ")))
print(f"Самое большое число: ", max(analyzer_list))
print(f"Самое маленькое число: ", min(analyzer_list))
print(f"Сумма: ", sum(analyzer_list))
print(f"Среднее арифметическое: ", sum(analyzer_list)/len(analyzer_list))