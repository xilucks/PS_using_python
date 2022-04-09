import heapq
import sys

N, M, R = map(int, input().split())
INF = int(1e9)

item = list(map(int, sys.stdin.readline().strip().split()))

graph = [[] for _ in range(N + 1)]


for _ in range(R):
    start, target, value = map(int, input().split())

    graph[start].append([target, value])
    graph[target].append([start, value])


def dijk(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return distance

ans = 0

for i in range(1, N):
    arr = dijk(i)
    tmp = 0
    for j in range(len(arr)):
        if arr[j] <= M:
            tmp += item[j-1]
    ans = max(ans, tmp)

print(ans)

