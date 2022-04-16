import heapq
import sys
from queue import PriorityQueue

N = int(input())

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

case = 1
while not N == 0:
    arr = []
    visit = [[False] * N for _ in range(N)]
    q = []

    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().strip().split())))

    heapq.heappush(q, [arr[0][0], 0, 0])
    visit[0][0] = True

    while q:
        money, y, x = heapq.heappop(q)

        if y == N-1 and x == N-1:
            print("Problem {}: {}".format(case, money))
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue

            if visit[ny][nx]:
                continue

            heapq.heappush(q, [money + arr[ny][nx], ny, nx])
            visit[ny][nx] = True

    N = int(input())
    case += 1



