board = [['-' for _ in range(3)] for _ in range(3)]
"""Переменная для создания пустого игрового поля"""


def create_gaming_field(board):
    """Функция создает игровое поле 3х3 с нумерацией строк, столбцов"""
    print('\n   0 1 2')
    for i in range(3):
        print(f'{i}  {" ".join(board[i])}')


def movement(current_player):
    """Функция получает ход от игрока в виде номера строки и столбца"""
    print(f'Игрок {current_player}, ваш ход.')
    row = int(input('Введите номер строки (0-2): '))
    column = int(input('Введите номер столбца (0-2): '))
    return row, column


def check_winner(board):
    """Функция проверяет, есть ли победитель или ничья на текущем игровом поле"""
    # Проверка строк на одинаковые символы
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]

    # Проверка столбцов на одинаковые символы
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]

    # Проверка диагоналей на одинаковые символы
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]

    # Проверка на ничью
    if all(cell != '-' for row in board for cell in row):
        return 'Ничья!'

    return None


def play_the_game():
    """Функция реализации игры"""
    print('Игра в крестики-нолики. Игроки по очереди вводят координаты строки, столбца')
    current_player = 'X'  # X ходит первым

    while True:
        create_gaming_field(board)
        row, column = movement(current_player)

        # Проверка ввода координат
        if 0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == '-':
            board[row][column] = current_player  # Сохраняем ход на поле
        else:
            print("Некорректный ход! Попробуйте еще раз.")
            continue

        result = check_winner(board)
        if result:
            create_gaming_field(board)
            if result == 'Ничья!':
                print('Ничья!')
            else:
                print(f'Победил игрок {result}!')
            break

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"


play_the_game()















