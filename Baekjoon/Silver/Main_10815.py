import collections
import sys

n = int(input())

dct = collections.defaultdict(int)

nums = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    dct[nums[i]] += 1

m = int(input())

ans = []
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    if dct[num] == 0:
        ans.append(0)
    else:
        ans.append(1)

print(*ans)