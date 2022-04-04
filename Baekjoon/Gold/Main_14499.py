import sys

N, M, y, x, K = map(int,input().split())

arr = []

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(tmp)

orders = list(map(int, sys.stdin.readline().strip().split()))
move = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]

# 좌측, 맨위, 우측, 앞면, 아래면, 뒷면
dice = [0 for _ in range(6)]

dice[4] = arr[y][x]

for order in orders:
    ny = y + move[order][0]
    nx = x + move[order][1]

    if nx < 0 or ny < 0 or ny >= N or nx >= M:
        continue

    #동
    if order == 1:
        dice = [dice[4], dice[0], dice[1], dice[3], dice[2], dice[5]]
    #서
    elif order == 2:
        dice = [dice[1], dice[2], dice[4], dice[3], dice[0], dice[5]]
    #북
    elif order == 3:
        dice = [dice[0], dice[3], dice[2], dice[4], dice[5], dice[1]]
    #남
    else:
        dice = [dice[0], dice[5], dice[2], dice[1], dice[3], dice[4]]

    if arr[ny][nx] == 0:
        arr[ny][nx] = dice[4]
    else:
        dice[4] = arr[ny][nx]
        arr[ny][nx] = 0

    y = ny
    x = nx

    print(dice[1])


