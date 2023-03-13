import collections
import sys

input_list = collections.deque(sys.stdin.readline().strip() for _ in range(36))

def solution(move_list):
    now_x, now_y = 0, 0
    start_x, start_y = 0, 0
    isVail = True
    isReturn = False
    visitDict = collections.defaultdict(int)

    knight_moving = [[2, 1], [-2, 1], [1, -2], [1, 2], [-1, 2], [-1, -2], [2, -1], [-2, -1]]

    while isVail and move_list:
        next_move = move_list.popleft()
        move_x, move_y = next_move[0], next_move[1]

        if now_x == 0 and now_y == 0:
            now_x = x_calculate(move_x)
            now_y = int(move_y)
            start_x = x_calculate(move_x)
            start_y = int(move_y)

            visitDict[next_move] += 1

        else:
            isMove = False
            target_x = x_calculate(move_x)
            target_y = int(move_y)

            for moving in knight_moving:
                x_moving, y_moving = moving[0], moving[1]

                if now_x + x_moving == target_x and now_y + y_moving == target_y:
                    isMove = True
                    now_x, now_y = target_x, target_y
                    visitDict[next_move] += 1
                    break

            if not isMove:
                isVail = False

    for moving in knight_moving:
        x_moving, y_moving = moving[0], moving[1]

        if now_x + x_moving == start_x and now_y + y_moving == start_y:
            isReturn = True
            break

    if isVail and len(visitDict.keys()) == 36 and isReturn:
        print('Valid')

    else:
        print('Invalid')

    return


def x_calculate(x):
    x_index = ['A', 'B', 'C', 'D', 'E', 'F']

    for index, index_name in enumerate(x_index):
        if index_name == x:
            return int(index + 1)


solution(input_list)