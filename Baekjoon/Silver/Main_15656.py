import sys

N, M = input().split()
N, M = int(N), int(M)

nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()
arr = []
for i in range(N):
    arr.append(0)
def dfs(x: int) -> int:
    if x == M :
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in nums:
        arr[x] = i
        dfs(x+1)
        arr[x] = 0

dfs(0)