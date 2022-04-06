import sys

N, M = map(int, input().split())

arr = []
dp = [[0] * M for _ in range(N)]

ans = 0

for _ in range(N):
    l = list(map(int, sys.stdin.readline().strip()))
    arr.append(l)

for i in range(N):
    if arr[i][0] == 1:
        dp[i][0] = 1
        ans = 1

for j in range(M):
    if arr[0][j] == 1:
        dp[0][j] = 1
        ans = 1

for i in range(1, N):
    for j in range(1, M):
        if arr[i][j] == 1:
            dp[i][j] = 1

        if arr[i][j] != 0 and dp[i-1][j] != 0 and dp[i][j-1] != 0 and dp[i-1][j-1] != 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        ans = max(ans, dp[i][j])

print(int(ans)**2)


