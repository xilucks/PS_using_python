import sys

N, M = input().split()
N, M = int(N), int(M)

nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()
arr = []
visit = []

for i in range(N):
    arr.append(-1)
    visit.append(False)

def dfs(x: int) -> int :
    if x == M:
        for i in range(M):
            print(arr[i], end = ' ')
        print("")
        return

    for j in range(N):
       if (not visit[j]):
           arr[x] = nums[j]
           visit[j] = True
           dfs(x + 1)
           arr[x] = 0
           visit[j] = False

dfs(0)