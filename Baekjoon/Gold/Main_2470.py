import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().strip().split()))

nums.sort()

l,r = 0,len(nums)-1
ansl, ansr = l, r

target = nums[l] + nums[r]
while l<r :
    tmp = nums[l] + nums[r]
    if abs(tmp) < abs(target) :
        target = tmp
        ansl = l
        ansr = r

    if tmp > 0 :
        r -= 1
    else :
        l += 1

print(nums[ansl],nums[ansr])
