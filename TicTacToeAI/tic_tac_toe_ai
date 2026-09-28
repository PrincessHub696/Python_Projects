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

def player_move(board):
    while True:
        try:
            row = int(input("Введите номер строки (1-3): ")) - 1
            col = int(input("Введите номер столбца (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Эта клетка уже занята!")
        except (ValueError, IndexError):
            print("Неверный ввод! Введи числа от 1 до 3.")

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

def computer_move(board):
    # Проверка, может ли компьютер победить
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_win(board, "O"):
                    return
                board[i][j] = " "

    # Проверка, может ли игрок победить и блокировка хода игроку
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_win(board, "X"):
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    # Занимаем центр, если свободен
    if board[1][1] == " ":
        board[1][1] = "O"
        return

    # Занимаем любой свободный угол
    for i in [0, 2]:
        for j in [0, 2]:
            if board[i][j] == " ":
                board[i][j] = "O"
                return

    # Занимаем любую свободную клетку
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                return

while True:
    print_board(board)

    player_move(board)
    if check_win(board, "X"):
        print("Ты победил!")
        break
    if is_full(board):
        print("Ничья!")
        break

    print_board(board)

    computer_move(board)
    if check_win(board, "O"):
        print("Компьютер победил!")
        break
    if is_full(board):
            print("Ничья!")
            break
