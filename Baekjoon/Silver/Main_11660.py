import sys

N, M = sys.stdin.readline().split()
N, M = int(N), int(M)
arr = []

for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

dp = [[0]*N for i in range(N)]

for x in range(N):
    for y in range(N):
        if x == 0 and y == 0:
            dp[x][y] = arr[x][y]
        elif x == 0 and y != 0:
            dp[x][y] = arr[x][y] + dp[x][y-1]
        elif y == 0 and x != 0:
            dp[x][y] = arr[x][y] + dp[x-1][y]
        else:
            dp[x][y] = arr[x][y] + dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]


for i in range(M):
    X1, Y1, X2, Y2 = sys.stdin.readline().split()
    X1, Y1, X2, Y2 = int(X1)-1, int(Y1)-1, int(X2)-1, int(Y2)-1
    if X1 == X2 and Y1 == Y2 :
        ans = arr[X1][Y1]
    elif X1 == 0 and Y1 == 0 :
        ans = dp[X2][Y2]
    elif Y1 == 0:
        ans = dp[X2][Y2] - dp[X1-1][Y2]
    elif X1 == 0 :
        ans = dp[X2][Y2] - dp[X2][Y1-1]
    else:
        ans = dp[X2][Y2] - dp[X1-1][Y2] - dp[X2][Y1-1] + dp[X1-1][Y1-1]

    print(ans)