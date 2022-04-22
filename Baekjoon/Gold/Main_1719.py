N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N+1)]
tmp = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    start, end, dist = map(int, input().split())
    graph[start][end] = min(dist, graph[start][end])
    graph[end][start] = min(dist, graph[end][start])
    tmp[start][end] = end
    tmp[end][start] = start

for stop in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if graph[start][end] > graph[start][stop] + graph[stop][end]:
                graph[start][end] = graph[start][stop] + graph[stop][end]
                tmp[start][end] = tmp[start][stop]
            else:
                continue


for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j :
            print('-', end = ' ')
            continue
        print(tmp[i][j], end=' ')
    print()