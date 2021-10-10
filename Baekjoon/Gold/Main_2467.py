import sys

N = int(input())

nums = list(map(int,sys.stdin.readline().strip().split()))

l = 0
r = len(nums)-1
max = nums[l] + nums[r]
ansl, ansr = l, r
while l < r:
    sum = nums[l] + nums[r]
    if abs(max) >= abs(sum):
        max = sum
        ansl = l
        ansr = r
    if sum < 0:
        l += 1
    else:
        r -= 1

print(nums[ansl], nums[ansr])

