import sys


def input_weather():
    H, W = map(int, sys.stdin.readline().split())
    weather = []
    move_map = []
    for _ in range(H):
        weather_string = sys.stdin.readline().strip()
        weather.append(list(weather_string))
        move_map.append([-1] * W)

    return [weather, move_map]


def cloud_move(y, x, move_map, move_count):
    if x >= len(move_map[0]) or move_map[y][x] != -1:
        return move_map

    if move_count == 0 and move_map[y][x] == -1:
        move_map[y][x] = 0

    else:
        move_map[y][x] = move_count

    return cloud_move(y, x + 1, move_map, move_count + 1)


def solution():
    [weather, move_map] = input_weather()

    for i in range(len(weather)):
        for j in range(len(weather[0]) - 1, -1, -1):
            if weather[i][j] == 'c':
                move_map = cloud_move(i, j, move_map, 0)

    for i in range(len(move_map)):
        print(*move_map[i])


solution()