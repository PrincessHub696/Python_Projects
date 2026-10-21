def evaluate_rpn(expression):
    stack = []

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b

            stack.append(result)

    return stack[0]

# Проверка работы
expression = input("Введите выражение в ОПЗ (например, '2 3 +'): ")
result = evaluate_rpn(expression)
print(f"Результат: {result}")