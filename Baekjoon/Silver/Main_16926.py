import sys


def solve():
    arr, turn_num = input_arr()
    result = rotation(arr, turn_num)

    for y in range(len(result)):
        print(*result[y])


def input_arr():
    y_len, x_len, turn_num = map(int, sys.stdin.readline().split())
    arr = []

    for _ in range(y_len):
        arr.append(list(map(int, sys.stdin.readline().split())))

    return arr, turn_num


def rotation(arr, turn_num):
    for _ in range(turn_num):
        turn(arr)

    return arr


def turn(arr):
    for min_len in range(min(len(arr), len(arr[0])) // 2):
        y, x = min_len, min_len
        value = arr[y][x] # 0,0 1,1, ..etc 부터 시작

        for target_y in range(min_len + 1, len(arr) - min_len): # 아래로
            y = target_y
            prev_value = arr[y][x]
            arr[y][x] = value
            value = prev_value

        for target_x in range(min_len + 1, len(arr[0]) - min_len): #오른쪽으로
            x = target_x
            prev_value = arr[y][x]
            arr[y][x] = value
            value = prev_value

        for target_y in range(min_len + 1, len(arr) - min_len): #위로
            y = len(arr) - target_y - 1
            prev_value = arr[y][x]
            arr[y][x] = value
            value = prev_value

        for target_x in range(min_len + 1, len(arr[0]) - min_len): #왼쪽으로
            x = len(arr[0]) - target_x - 1
            prev_value = arr[y][x]
            arr[y][x] = value
            value = prev_value

    return arr


solve()