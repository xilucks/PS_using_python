N = int(input())

dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i-1] + dp[i-2]

if N == 1:
    print(4)
else:
    print((dp[N-1] + dp[N-2] + dp[N-1]) * 2)