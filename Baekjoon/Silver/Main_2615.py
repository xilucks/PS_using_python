import sys


def read_map():
    arr = []
    visit = []

    line = list(map(int, sys.stdin.readline().split()))
    while len(line) > 0:
        arr.append(line)
        visit.append([0] * (len(line)))
        line = list(map(int, sys.stdin.readline().split()))

    return [arr, visit]


def search(y, x, ground, visit, color, count, ans_arr, moving):
    search_list = [[1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, -1], [-1, 0], [1, 1]]
    ans_arr.append([y, x])
    if count > 5 or visit[y][x] == -1:
        print('over start')
        visit[y][x] = -1
        # return None
    else:
        visit[y][x] = True

    if count == 1:
        for move in search_list:
            ny, nx = y + move[0], x + move[1]
            print('new', y, x, ny, nx, visit[y][x])

            if ny < 0 or ny >= len(visit) or nx < 0 or nx >= len(visit[0]) or visit[y][x] == -1:
                continue
            print(visit[0][nx])

            if ground[ny][nx] == color:
                result = search(ny, nx, ground, visit, color, count + 1, ans_arr, [move[0], move[1]])
                if result is not None and result[0] != 0 and len(result[1]) == 5:
                    return result
                else:
                    continue
            print('----')

    else:
        ny, nx = y + moving[0], x + moving[1]
        print('search', y, x, ny, nx)
        if ny < 0 or ny >= len(visit) or nx < 0 or nx >= len(visit[0]):
            print('pass')
            if count == 5:
                print('ans', ans_arr, count)
                return [color, ans_arr]
            return None
        # print(visit[0][nx])
        # print(ny)
        # print(ground[ny][0])
        # print(visit[ny][0])
        if count == 5 and (visit[ny][nx] == -1 or ground[ny][nx] == color):
            return None

        if ground[ny][nx] == color and visit[ny][nx] != -1:
            print('same color')
            if count > 5:
                print('over')
                visit[ny][nx] = -1
                search(ny, nx, ground, visit, color, count + 1, ans_arr, [moving[0], moving[1]])
                return None
            result = search(ny, nx, ground, visit, color, count + 1, ans_arr, [moving[0], moving[1]])
            print('res', result)
            return result
        elif visit[ny][nx] != -1:
            if count == 5:
                print('good', ans_arr)
                return [color, ans_arr]
        else:
            return None


def solution():
    [ground, visit] = read_map()
    ans_color = 0
    ans_y, ans_x = 0, 0

    for y in range(len(ground)):
        for x in range(len(ground[0])):
            if ground[y][x] == 1 or ground[y][x] == 2:
                ans_arr = []
                ans_color = search(y, x, ground, visit, ground[y][x], 1, ans_arr, [])
                if ans_color != 0 and ans_color is not None:
                    ans_y, ans_x = y, x
                    break
        if ans_color != 0 and ans_color is not None:
            break

    # print(ans_color)

    if ans_color is None or ans_color == 0:
        print(0)
    else:
        print(ans_color)
        ans_color[1].sort(key=lambda x: (x[1], x[0]))
        [ans_y, ans_x] = ans_color[1][0]
        print(ans_color[0])
        print(ans_y + 1, ans_x + 1)

    for i in range(len(visit)):
        print(visit[i])


solution()