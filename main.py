# Создаем пустую игровую доску 3x3
board = [[" " for _ in range(3)] for _ in range(3)]


# Функция для отображения игровой доски
def display_board(board):
    for row in board:
        print(" ".join(row))
        print("-" * 7)


# Функция для проверки выигрышной комбинации
def check_win(board, player):
    # Проверяем выигрышные комбинации по горизонтали
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Проверяем выигрышные комбинации по вертикали
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # Проверяем выигрышные комбинации по диагоналям
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board) - i - 1] == player for i in range(len(board))):
        return True

    return False


# Функция для осуществления хода игрока
def make_move(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


# Основной игровой цикл
current_player = "x"
while True:
    # Отображаем игровую доску
    display_board(board)

    # Ход игрока
    while True:
        row = int(input("Выберите номер строки (0-2): "))
        col = int(input("Выберите номер столбца (0-2): "))
        if make_move(board, current_player, row, col):
            break
        else:
            print("Неверный ход. Попробуйте еще раз.")

    # Проверяем выигрышную комбинацию
    if check_win(board, current_player):
        print("Игрок", current_player, "победил!")
        break

    # Проверяем ничью
    if all(cell != " " for row in board for cell in row):
        print("Ничья!")
        break

    # Переключаем игроков
    current_player = "O" if current_player == "X" else "X"