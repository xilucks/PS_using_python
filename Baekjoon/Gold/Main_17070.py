import sys
from collections import deque

N = int(input())
arr = []
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

# 0 = 대각 1 = 세로 2 = 가로
col = 1

dp[2][0][1] = 1

for i in range(2, N):
    if arr[0][i] == 0:
        dp[2][0][i] = dp[2][0][i-1]

for i in range(1, N):
    for j in range(2, N):
        if arr[i][j] == 0 and arr[i-1][j-1] == 0 and arr[i][j-1] == 0 and arr[i-1][j] == 0:
            dp[0][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

        if arr[i][j] == 0:
            dp[1][i][j] = dp[0][i-1][j] + dp[1][i-1][j]
            dp[2][i][j] = dp[0][i][j-1] + dp[2][i][j-1]


ans = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]

print(ans)
