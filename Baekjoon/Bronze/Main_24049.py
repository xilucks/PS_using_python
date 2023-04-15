import sys


def input_data():
    N, M = map(int, sys.stdin.readline().split())
    y = list(map(int, sys.stdin.readline().split()))
    x = list(map(int, sys.stdin.readline().split()))

    return [N, M, y, x]


def search(garden, y, x):
    upper_location = garden[y - 1][x] if garden[y - 1][x] != -1 else search(garden, y-1, x)
    left_location = garden[y][x - 1] if garden[y][x - 1] != -1 else search(garden, y, x-1)

    return 0 if upper_location == left_location else 1


def full_search(garden, y, x):
    for y_index in range(1, y + 1):
        for x_index in range(1, x + 1):
            upper_location = garden[y_index - 1][x_index]
            left_location = garden[y_index][x_index - 1]
            garden[y_index][x_index] = 0 if upper_location == left_location else 1

    return garden[y][x]


def solution():
    [N, M, y, x] = input_data()
    garden = [[-1] * (M + 1) for _ in range(N + 1)]

    for index, y_value in enumerate(y):
        garden[index + 1][0] = y_value

    for index, x_value in enumerate(x):
        garden[0][index + 1] = x_value

    ans = full_search(garden, N, M)
    print(ans)


solution()
