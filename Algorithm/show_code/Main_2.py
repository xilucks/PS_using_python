import sys
from collections import deque

N, Q = map(int, input().split())

nums = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(len(nums)+1)]


for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for _ in range(Q):
    start, end = map(int, input().split())

    queue = deque()
    queue.append(start)

    visit = [False for _ in range(len(nums) + 1)]
    visit[start] = True

    ans: str = str(nums[start-1])

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:

            if not visit[next_node]:
                visit[next_node] = True
                ans += str(nums[next_node-1])
                queue.append(next_node)

        if node == end:
            break

    print(int(ans) % 1000000007)
