import sys

N, M = input().split()
N, M = int(N), int(M)

nums = list(map(int, sys.stdin.readline().strip().split()))
arr = []
for i in range(N) :
    arr.append(0)
nums.sort()
def dfs(x : int, y: int):
    if x == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(y,N):
        arr[x] = nums[i]
        dfs(x+1,i)


dfs(0,0)
