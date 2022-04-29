import sys
from collections import deque

N = int(input())

arr = deque(map(int, sys.stdin.readline().split()))
index = deque()
ans = []
move = 1
for i in range(N):
    index.append(i+1)

while True:
    if move < 0:
        move = arr.pop()
        ans.append(index.pop())

    else:
        move = arr.popleft()
        ans.append(index.popleft())
        
    if not arr:
        break

    if move < 0:
        for _ in range(abs(move)-1):
            print('aa')
            print(arr)
            arr.append(arr.popleft())
            index.append(index.popleft())
            print(arr)
    else:
        for _ in range(abs(move)-1):
            arr.appendleft(arr.pop())
            index.appendleft(index.pop())

print(*ans)