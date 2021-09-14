#빗물 트래핑
#높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
import sys

height = list(map(int, sys.stdin.readline().strip().split()))



# 투포인터
volume = 0
left = 0
right = len(height)-1
left_max, right_max = height[left], height[right]

while left < right :
    left_max = max(height[left], left_max)
    right_max = max(height[right], right_max)

    if left_max <= right_max :
        volume += left_max - height[left]
        left += 1
    else:
        volume += right_max - height[right]
        right -= 1

print(volume)


#스택 쌓기

stack = []
volume = 0

for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()

        if not len(stack):
            break

        distance = i - stack[-1] -1
        waters = min(height[i], height[stack[-1]]) - height[top]

        volume += distance * waters

    stack.append(i)

print(volume)