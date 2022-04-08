import heapq

N = int(input())
M = int(input())
INF = int(1e9)

distance = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, target, value = map(int, input().split())
    graph[start].append([target, value])

def dijk(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


A, B = map(int, input().split())

dijk(A)

print(distance[B])




