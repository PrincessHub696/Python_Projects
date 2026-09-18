board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(board):
    print("  1   2   3")
    for i, row in enumerate(board, 1):
        print(f"{i} {row[0]} | {row[1]} | {row[2]}")
        if i < 3:
            print(" ---+---+---")

def make_move(board, player):
    row = int(input("Введите номер строки (1-3): "))
    col = int(input("Введите номер столбца (1-3): "))
    board[row - 1][col - 1] = player  # Индексы начинаются с 0 и ставим символ игрока в нужную клетку

def check_win(board, player):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
        
    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

while True:
    print_board(board)

    make_move(board, "X")
    if check_win(board, "X"):
        print("Победил X!")
        break
    if is_full(board):
        print("Ничья!")
        break

    print_board(board)

    make_move(board, "O")
    if check_win(board, "O"):
        print("Победил O!")
        break
    if is_full(board):
            print("Ничья!")
            break