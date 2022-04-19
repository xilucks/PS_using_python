import heapq
import sys

N = int(input())

arr = []

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
visit = [[False] * N for _ in range(N)]
q = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

heapq.heappush(q, [0, 0, 0])

while q:
    ind, y, x = heapq.heappop(q)

    if visit[y][x]:
        continue

    if y == N-1 and x == N-1:
        print(ind)
        break

    visit[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue

        if visit[ny][nx]:
            continue

        heapq.heappush(q, [max(abs(arr[y][x]-arr[ny][nx]), ind), ny, nx])
