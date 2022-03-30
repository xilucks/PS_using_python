# 칸 개수
from collections import deque

N = int(input())

arr = [[0] * (N + 1) for _ in range(N + 1)]

# 사과 개수
K = int(input())
apple = []
for _ in range(K):
    x, y = map(int, input().split())
    apple.append([x, y])

L = int(input())

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
state = 1
# 움직임 계산 카운트
move_count = 0
moves = []
for _ in range(L):
    tmp = list(map(str, input().split()))
    moves.append([int(tmp[0]), tmp[1]])

snake = deque()

snake.append([1, 1])

while True:
    y, x = snake[-1][0], snake[-1][1]
    ny = y + d[state][0]
    nx = x + d[state][1]

    tmp = [ny, nx]
    move_count += 1

    if ny > N or nx > N or ny <= 0 or nx <= 0:
        break

    if tmp in snake:
        break

    if tmp in apple:
        snake.append(tmp)
        apple.remove(tmp)

    else:
        snake.append(tmp)
        snake.popleft()

    for i in range(len(moves)):
        if move_count == moves[i][0] and moves[i][1] == 'L':
            state = (state+1) % 4
        if move_count == moves[i][0] and moves[i][1] == 'D':
            state = (state+3) % 4


print(move_count)



