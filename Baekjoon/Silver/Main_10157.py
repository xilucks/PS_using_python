import sys


def solution():
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    target_index = [0, 0]

    X, Y = map(int, sys.stdin.readline().split())
    visit = []

    for _ in range(Y):
        visit.append([0] * X)

    target = int(sys.stdin.readline())

    count = 1
    direction = 0

    index_y, index_x = Y, 0

    change_count = 0

    while count != target + 1:
        if change_count > 4:
            break
        [move_y, move_x] = moves[direction]
        next_y, next_x = index_y + move_y, index_x + move_x
        if next_y < 0 or next_y >= Y or next_x < 0 or next_x >= X or visit[next_y][next_x] != 0 :
            direction = (direction + 1) % 4
            change_count += 1
            continue

        index_y, index_x = next_y, next_x
        visit[index_y][index_x] = count
        count += 1
        change_count = 0

        target_index = [index_y, index_x]

    if change_count > 4:
        print(0)

    else:
        print(index_x + 1, abs(Y - index_y))


solution()
