import sys

n = int(input())
nums = list(map(int,sys.stdin.readline().strip().split()))
nums.sort()
start = 0
end = len(nums)
ans = 0

for i in range(n):
    tmp = nums[:i] + nums[i+1:]
    left, right = 0, len(nums)-2
    while left < right:
        tmpnum = tmp[left] + tmp[right]
        if tmpnum == nums[i]:
            ans += 1
            break
        elif tmpnum > nums[i]:
            right -= 1
        elif tmpnum < nums[i]:
            left += 1

print(ans)




