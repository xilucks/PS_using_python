N = int(input())
M = int(input())

INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    start, end, dist = map(int, input().split())
    graph[start][end] = min(dist, graph[start][end])


for stop in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            graph[start][end] = min(graph[start][end], graph[start][stop] + graph[stop][end])


for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

