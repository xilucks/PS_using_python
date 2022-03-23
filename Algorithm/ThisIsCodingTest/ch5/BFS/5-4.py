from collections import deque

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0


def bfs(y, x) -> int:
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            if arr[ny][nx] == 0:
                continue

            if arr[ny][nx] == 1:
                arr[ny][nx] = arr[y][x] + 1
                queue.append((ny, nx))

    return arr[N - 1][M - 1]


print(bfs(0, 0))
