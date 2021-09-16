import sys

N, M = input().split()
N, M= int(N), int(M)
nums = list(map(int, sys.stdin.readline().strip().split()))
arr = []
nums.sort()

for i in range(N):
    arr.append(0)

def dfs(x: int, y:int) -> int:
    if x == M:
        for i in range(M):
            print(arr[i], end=' ')
        print("")
        return

    for j in range(y, N):
        arr[x] = nums[j]
        dfs(x+1, j+1)
        arr[x] = 0


dfs(0,0)