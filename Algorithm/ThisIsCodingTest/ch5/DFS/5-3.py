import sys

N, M = map(int, input().split())

print(N, M)

arr = []
for i in range(N):
    arr.append(list(map(int, input())))

print(arr)

def dfs(y, x):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False

    if arr[y][x] == 0:
        arr[y][x] = 1
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        return True
    return False


ans = 0

for i in range(M):
    for j in range(N):
        if dfs(i, j):
            ans += 1

print(ans)
