import sys

n, m = map(int, sys.stdin.readline().split())

ans = 0
for i in range(m):
    nums = list(map(int, sys.stdin.readline().split()))

    minnum = min(nums)

    ans = max(ans, minnum)

print(ans)