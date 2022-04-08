import heapq

N, M = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(N+1)]


for _ in range(M):
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


v1, v2 = map(int, input().split())

list_full = dijk(1)
list_v1 = dijk(v1)
list_v2 = dijk(v2)

v1_length = list_full[v1] + list_v1[v2] + list_v2[N]
v2_length = list_full[v2] + list_v2[v1] + list_v1[N]

ans = min(v1_length, v2_length)

print(ans if ans < INF else -1)
