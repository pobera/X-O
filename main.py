import random


# Функция для создания игрового поля
def create_board():
    board = [[' ' for _ in range(6)] for _ in range(6)]
    return board


# Функция для вывода игрового поля
def print_board(board):
    print('  |1| 2| 3| 4| 5| 6|  ')
    for i in range(6):
        print(str(i+1) + ' |' + ' |'.join(board[i]) + '|')


# Функция для размещения кораблей на игровом поле
def place_ships(board):
    ship_sizes = [3, 2, 2, 1, 1, 1, 1]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for size in ship_sizes:
        while True:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            direction = random.choice(directions)

            if x + (size - 1) * direction[0] not in range(6) or y + (size - 1) * direction[1] not in range(6):
                continue

            overlap = False
            for i in range(size):
                if board[x + i * direction[0]][y + i * direction[1]] != ' ':
                    overlap = True
                    break

            if overlap:
                continue

            for i in range(size):
                board[x + i * direction[0]][y + i * direction[1]] = '#'

            break


# Функция для осуществления хода игрока
def player_turn(board):
    while True:
        try:
            x = int(input('Введите номер строки (от 1 до 6): ')) - 1
            y = int(input('Введите номер столбца (от 1 до 6): ')) - 1

            if x not in range(6) or y not in range(6) or board[x][y] in ['X', 'O']:
                continue


            break
        except ValueError:
            print('Ошибка! Попробуйте еще раз.')

    if board[x][y] == '#':
        board[x][y] = 'X'
        print('Попадание!')
    else:
        board[x][y] = 'T'
        print('Мимо.')


# Функция для осуществления хода ИИ
def ai_turn(board):
    while True:
        x = random.randint(0, 5)
        y = random.randint(0, 5)

        if board[x][y] in ['X', 'O']:
            continue

        break

    if board[x][y] == '#':
        board[x][y] = 'X'
        print('ИИ попал!')
    else:
        board[x][y] = '0'
        print('ИИ мимо.')


# Функция для проверки окончания игры
def game_over(board):
    for row in board:
        if '#' in row:
            return False

    return True


# Основная функция игры
def play_game():
    board = create_board()
    place_ships(board)

    while True:
        print_board(board)
        print('Ваш ход:')
        player_turn(board)

        if game_over(board):
            print_board(board)
            print('Вы победили!')
            break

        print('Ход ИИ:')
        ai_turn(board)

        if game_over(board):
            print_board(board)
            print('ИИ победил!')
            break


# Запуск игры
play_game()