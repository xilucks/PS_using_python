import sys

nums = list(map(int, sys.stdin.readline().strip().split()))
stack = []
answer = [0] * len(nums)

for i, cur in enumerate(nums):
    while stack and cur > nums[stack[-1]]:
        index = stack.pop()
        answer[index] = i - index

    stack.append(i)

print(answer)