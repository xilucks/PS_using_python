import sys

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
visit = [[0] * M for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

#북, 동, 남, 서
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
turn_count = 0
ans = 1

visit[r][c] = 1

while True:
    d = (d + 3) % 4
    nr = r + moves[d][0]
    nc = c + moves[d][1]

    if arr[nr][nc] == 0 and visit[nr][nc] == 0:
        visit[nr][nc] = 1
        r = nr
        c = nc
        turn_count = 0
        ans += 1
        continue

    else:
        turn_count += 1

    if turn_count == 4:
        nr = r - moves[d][0]
        nc = c - moves[d][1]

        if arr[nr][nc] == 0:
            r = nr
            c = nc
            turn_count = 0
        else:
            break


print(ans)
