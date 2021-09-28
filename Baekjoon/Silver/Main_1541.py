import sys
from collections import deque

str = sys.stdin.readline().strip()
nums = deque()
cal = []
tmp = ''
tmpnum = 0
for ch in range(len(str)) :
    if not (str[ch] == '+' or str[ch] =='-') :
        tmp += str[ch]
    if str[ch] == '+' or str[ch] == '-' or ch == len(str)-1:
        nums.append(int(tmp))
        tmp = ''
        if not ch == len(str)-1:
            cal.append(str[ch])


X = True
for i in range(len(cal)):
    if cal[i] == '-':
        X = False
    if X == True :
        tmp = nums.popleft() + nums.popleft()
    else :
        tmp = nums.popleft() - nums.popleft()

    nums.appendleft(tmp)

print(nums[0])


