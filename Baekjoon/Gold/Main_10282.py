import heapq

T = int(input())

INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    distance[start] = 0

    heapq.heappush(q, [0, start])

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

def solve(computer, line, hack):

    graph = [[] for _ in range(computer + 1)]
    distance = [INF] * (computer + 1)

    for _ in range(line):
        a, b, s = map(int, input().split())

        graph[b].append([a, s])

    arr = dijkstra(hack, graph, distance)

    hacked, time = 0, 0

    for i in arr:
        if i == INF:
            continue
        hacked += 1
        time = max(time, i)

    return hacked, time


for _ in range(T):
    n, d, c = map(int, input().split())

    hacked, time = solve(n, d, c)
    print(hacked, time)
