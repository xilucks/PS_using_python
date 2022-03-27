import sys

N = int(input())

nums = list(map(int, sys.stdin.readline().strip().split()))

d = [0] * N

for i in range(0, N):
    if i == 0:
        d[i] = nums[0]

    elif i == 1:
        d[i] = max(nums[0], nums[1])

    else:
        d[i] = max(d[i-1], d[i-2] + nums[i])

