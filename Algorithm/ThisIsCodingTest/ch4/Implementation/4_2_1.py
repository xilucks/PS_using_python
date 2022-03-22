#my solution

N = input()

x, y = int(ord(N[0])) - int(ord('a')) + 1, int(N[1])
moving = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (2, -1), (1, 2), (1, -2)]

ans = 0

for move in moving:
    dx = move[0]
    dy = move[1]

    nx = x + dx
    ny = y + dy

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue

    ans += 1

print(ans)


