import sys

nums = list(map(int, sys.stdin.readline().strip().split()))

sum = 0
pair = []
nums.sort()

for n in nums:
    pair.append(n)
    if len(pair) == 2:
        sum += min(pair)
        pair = []

print(sum)








