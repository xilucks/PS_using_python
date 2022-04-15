import heapq
import sys

N = int(input())

visit = [[False] * N for _ in range(N)]
arr = []
q = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

heapq.heappush(q, [0, 0, 0])

visit[0][0] = True

while q:
    count, y, x = heapq.heappop(q)

    if y == N-1 and x == N-1:
        print(count)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue

        if visit[ny][nx]:
            continue

        if arr[ny][nx] == 1:
            heapq.heappush(q, [count, ny, nx])

        else:
            heapq.heappush(q, [count+1, ny, nx])

        visit[ny][nx] = True




