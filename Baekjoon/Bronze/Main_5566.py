import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = []
dice = []
index = 0
count = 0

for _ in range(N):
    board.append(int(sys.stdin.readline().strip()))

for _ in range(M):
    dice.append(int(sys.stdin.readline().strip()))

for move in dice:
    count += 1
    index += move
    index += board[index] if index < N else 0
    if index >= N:
        break

print(count)
