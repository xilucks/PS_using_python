import collections


def solution(maps):
    queue = collections.deque()
    result_map = [[int(1e9)] * len(maps[0]) for _ in range(len(maps))]
    queue.append([0, 0])
    answer = bfs(queue, maps, result_map)

    return -1 if answer == int(1e9) else answer


def bfs(queue, maps, result_map):
    move_case = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result_map[0][0] = 1

    while queue:
        y, x = queue.popleft()

        for move in move_case:
            dy, dx = move[0], move[1]
            ny, nx = y + dy, x + dx

            if ny >= len(maps) or nx >= len(maps[0]) or ny < 0 or nx < 0:
                continue

            elif maps[ny][nx] == 1 and (result_map[ny][nx] == result_map[ny][nx] > result_map[y][x] + 1):
                result_map[ny][nx] = result_map[y][x] + 1

                queue.append([ny, nx])

    return result_map[len(maps) - 1][len(maps[0]) - 1]
