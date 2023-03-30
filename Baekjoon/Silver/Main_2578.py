import sys


def input_data():
    board = []
    numbers = []

    for _ in range(5):
        board.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(5):
        numbers.append(list(map(int, sys.stdin.readline().split())))

    return [board, numbers]


def search_board(board, number, y_checker_board, x_checker_board, left_cross_checker, right_cross_checker):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                if i == j:
                    left_cross_checker += 1

                if i + j == 4:
                    right_cross_checker += 1

                y_checker_board[i] += 1
                x_checker_board[j] += 1
                return y_checker_board, x_checker_board, left_cross_checker, right_cross_checker


def bingo_checker(y_checker_board, x_checker_board, left_cross_checker, right_cross_checker):
    bingo = 0

    if left_cross_checker == 5:
        bingo += 1

    if right_cross_checker == 5:
        bingo += 1

    for y in y_checker_board:
        if y == 5:
            bingo += 1

    for x in x_checker_board:
        if x == 5:
            bingo += 1

    if bingo >= 3:
        return True

    return False


def solution():
    board, numbers = input_data()
    y_checker_board, x_checker_board = [0 for _ in range(5)], [0 for _ in range(5)]
    left_cross_checker, right_cross_check = 0, 0
    count = 0
    bingo = 0

    for i in range(5):
        for j in range(5):
            y_checker_board, x_checker_board, left_cross_checker, right_cross_check = \
                search_board(board, numbers[i][j],
                             y_checker_board,
                             x_checker_board,
                             left_cross_checker,
                             right_cross_check)
            count += 1

            isBingo = bingo_checker(y_checker_board, x_checker_board, left_cross_checker, right_cross_check)

            if isBingo:
                return count


print(solution())

