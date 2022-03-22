#회전 (n+3)%4
x_len, y_len = map(int, input().split())

visit = [[0] * y_len for _ in range(x_len)]

x, y, see = map(int, input().split())

arr = []
for i in range(y_len):
    arr.append(list(map(int, input().split())))

count = 1
turn_count = 0
visit[y][x] = 1

while True:
    ny = y
    nx = x
    see = (see+3) % 4
    if see == 0:
        ny -= 1
    elif see == 1:
        nx += 1
    elif see == 2:
        ny += 1
    else:
        nx -= 1

    #움직임이 배열 밖으로 갈 때, 생략
    if ny < 0 or ny >= y_len or nx < 0 or nx >= x_len:
        continue

    if visit[ny][nx] == 0 and arr[ny][nx] == 0:
        y = ny
        x = nx
        visit[y][x] = 1
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        if arr[ny][nx] == 0:
            y = ny
            x = nx
            turn_count = 0
        else:
            break

print(count)

