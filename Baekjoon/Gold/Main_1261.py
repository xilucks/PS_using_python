import heapq
import sys

#M이 가로, N이 세로
M, N = map(int, input().split())

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

arr = []
visit = [[False] * M for _ in range(N)]
q = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

visit[0][0] = True
heapq.heappush(q, [0, 0, 0])

while q:
    count, y, x = heapq.heappop(q)

    if y == N - 1 and x == M - 1:
        print(count)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue

        if visit[ny][nx]:
            continue

        if arr[ny][nx] == 1:
            heapq.heappush(q, [count+1, ny, nx])

        else:
            heapq.heappush(q, [count, ny, nx])

        visit[ny][nx] = True
