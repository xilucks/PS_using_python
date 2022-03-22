#my solution
import sys

N = int(input())
y, x = 1, 1
move = list(sys.stdin.readline().strip().split())

for i in range(N+1):
    nx = x
    ny = y

    if move[i] == 'R':
        nx = nx + 1
    elif move[i] == 'L':
        nx = nx - 1
    elif move[i] == 'U':
        ny = ny - 1
    else:
        ny = ny + 1

    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x = nx
    y = ny

print(x,y)


