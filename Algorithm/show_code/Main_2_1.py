import sys
from collections import deque

def dfs(node, ans, end):
    if node == end:
        print(int(ans) % 1000000007)
        return

    for next_node in graph[node]:
        visit[node] = True
        if not visit[next_node] and graph[next_node]:
            visit[next_node] = True
            new_ans = ans + str(nums[next_node - 1])
            dfs(next_node, new_ans, end)
            visit[next_node] = False

    visit[node] = True

N, Q = map(int, input().split())

nums = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(len(nums) + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for _ in range(Q):
    start, end = map(int, input().split())

    visit = [False for _ in range(len(nums) + 1)]


    ans: str = str(nums[start - 1])

    dfs(start, ans, end)



