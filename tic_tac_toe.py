import random
def draw_board(board):
    for i in range(0,9,3):
        print('|', board[i], '|', board[i + 1], '|', board[i + 2], '|')

def get_player_move(board, player_symbol):
    while True:
        try:
            i = input("Введите номер ячейки (от 1 до 9): ")
            posit = random.choice([i for i in range(9) if board[i] == " "])
            if i and 1 <= int(i) <= 9:
                posit = int(i) - 1
                if board[posit] == " ":
                    board[posit] = player_symbol
                    break
                else:
                    print("Эта ячейка уже занята. Попробуйте еще раз.")
            else:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 9.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 9.")
    return int(i)

def get_computer_move(board, symbol):
    while True:
        free_i = [i for i, cell in enumerate(board) if cell == " "]
        if free_i:
            position = random.choice(free_i)
            board[position] = symbol
            return position


def check_win(board, player_symbol):
    combinations_win = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    for combination in combinations_win:
        position_1 = board[combination[0]]
        position_2 = board[combination[1]]
        position_3 = board[combination[2]]

        comparison_1 = (position_1 == player_symbol)
        comparison_2 = (position_2 == player_symbol)
        comparison_3 = (position_3 == player_symbol)

        if comparison_1 and comparison_2 and comparison_3:
            return True

    return False
def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player_symbol = "0"
    computer_symbol = "X"
    while True:
        draw_board(board)
        get_player_move(board, player_symbol)
        print("Доска после хода компьютера")


        if check_win(board, player_symbol):
            draw_board(board)
            print("Вы победили!")

            break
        get_computer_move(board, computer_symbol)
        if check_win(board, computer_symbol):
            draw_board(board)
            print("Компьютер победил. Попробуйте еще раз.")
            break
        if draw(board):
            draw_board(board)
            print("Ничья!")
            break



def draw(board):
    if " " not in board:
        return True
    return False

main()
