import heapq

V, E = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end, dist = map(int, input().split())
    graph[start][end] = dist

for way in range(1, V+1):
    for start in range(1, V+1):
        for end in range(1, V+1):
            graph[start][end] = min(graph[start][end], graph[start][way] + graph[way][end])

ans = INF

for i in range(1, V+1):
    ans = min(ans, graph[i][i])

if ans == INF:
    ans = -1

print(ans)