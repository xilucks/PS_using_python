#자신을 제외한 배열의 곱
# 나눗셈을을 하지 않고 O(n)의 풀이

import sys

nums = list(map(int, sys.stdin.readline().strip().split()))
ans = []
p = 1

for i in range(0,len(nums)):
    ans.append(p)
    p = p * nums[i]

p = 1

for i in range(len(nums)-1, -1 , -1):
    ans[i] = ans[i] * p
    p = p * nums[i]


print(ans)
