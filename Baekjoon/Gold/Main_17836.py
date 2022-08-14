import sys

N, M, T = map(int, sys.stdin.readline().split())
castle = []
move_result = [[int(1e9)] * M for _ in range(N)]
queue = []
ans = 0

for _ in range(N):
    castle.append(list(map(int, sys.stdin.readline().split())))

def start():
    move_result[0][0] = 0
    queue.append([0, 0])
    bfs()

    if move_result == int(1e9) or move_result[N-1][M-1] > T:
        return "Fail"
    else:
        return move_result[N-1][M-1]

def bfs():
    while queue:
        y, x = queue.pop()
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for move in moves:
            dy, dx = move[0], move[1]
            ny, nx = y + dy, x + dx
            jud_move(y, x, ny, nx)


def jud_move(y, x, ny, nx):
    if ny >= N or ny < 0 or nx >= M or nx < 0:
        return

    elif castle[ny][nx] != 1:
        if move_result[ny][nx] > move_result[y][x] + 1:
            queue.append([ny, nx])
            move_result[ny][nx] = move_result[y][x] + 1

        if castle[ny][nx] == 2:
            sword_moving(ny, nx)

def sword_moving(y, x):
    if move_result[N-1][M-1] > abs(y-(N-1)) + abs(x-(M-1)) + move_result[y][x]:
        move_result[N-1][M-1] = abs(y-(N-1)) + abs(x-(M-1)) + move_result[y][x]

print(start())