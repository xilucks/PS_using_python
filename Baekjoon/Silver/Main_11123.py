import collections
import sys


def input_data():
    case = int(sys.stdin.readline())
    maps = []

    for _ in range(case):
        y, x = map(int, sys.stdin.readline().split())
        field = []

        for _ in range(y):
            field.append(list(sys.stdin.readline().strip()))

        maps.append(field)

    return maps


def dfs(field, y, x):
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    for move in moves:
        ny = y + move[0]
        nx = x + move[1]

        if ny < 0 or ny >= len(field) or nx < 0 or nx >= len(field[0]):
            continue

        if field[ny][nx] == '#':
            field[ny][nx] = 'visit'
            dfs(field, ny, nx)


def bfs(field, y, x):
    queue = collections.deque()
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    queue.append([y, x])
    while queue:
        y, x = queue.popleft()

        for move in moves:
            ny = y + move[0]
            nx = x + move[1]

            if ny < 0 or ny >= len(field) or nx < 0 or nx >= len(field[0]):
                continue

            if field[ny][nx] == '#':
                field[ny][nx] = 'visit'
                queue.append([ny, nx])


def solution():
    maps = input_data()

    for case in range(len(maps)):
        field = maps[case]
        ans = 0

        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] == '#':
                    ans += 1
                    field[y][x] = 'visit'
                    bfs(field, y, x)
        print(ans)


solution()