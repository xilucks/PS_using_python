import heapq

v, e, p = map(int, input().split())

INF = int(1e9)
graph = [[] * (v+1) for _ in range(v+1)]


for _ in range(e):
    start, end, dist = map(int, input().split())
    graph[start].append([end, dist])
    graph[end].append([start, dist])

def dijkstra(start):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        value, now = heapq.heappop(q)

        if distance[now] < value:
            continue

        for i in graph[now]:
            new_dist = value + i[1]

            if new_dist < distance[i[0]]:
                distance[i[0]] = new_dist
                heapq.heappush(q, [new_dist, i[0]])

    return distance


full_dist = dijkstra(1)
gun_dist = dijkstra(p)

full = full_dist[v]
gun = full_dist[p] + gun_dist[v]

if full == gun:
    print("SAVE HIM")
else:
    print("GOOD BYE")