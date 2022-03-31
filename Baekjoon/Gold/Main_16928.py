import collections
from collections import deque

N, M = map(int, input().split())

ladder = collections.defaultdict(int)
snake = collections.defaultdict(int)

for _ in range(N):
    tmp = list(map(int, input().split()))
    ladder[tmp[0]] = tmp[1]

for _ in range(M):
    tmp = list(map(int, input().split()))
    snake[tmp[0]] = tmp[1]

distance = [0] * 101
visit = [False] * 101

queue = deque()


distance[0] = 0
distance[1] = 1

queue.append(1)

while queue:
    new_index = 0

    tmp = queue.popleft()

    if tmp == 100:
        break

    for i in range(1, 7):
        new_index = tmp + i

        if new_index > 100:
            break

        if visit[new_index]:
            continue

        if ladder.get(new_index):
            new_index = ladder[new_index]

        if snake.get(new_index):
            new_index = snake[new_index]

        if not visit[new_index]:
            visit[new_index] = True
            distance[new_index] = distance[tmp] + 1
            queue.append(new_index)

print(distance)
print(distance[100]-1)