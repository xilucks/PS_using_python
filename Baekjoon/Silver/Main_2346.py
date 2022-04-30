import sys
from collections import deque

n = int(input())

arr = deque(map(int, sys.stdin.readline().split()))
index = deque([i+1 for i in range(n)])
ans = []

move = arr.popleft()
ans.append(index.popleft())

while True:
    if not arr:
        break
    if move > 0:
        for _ in range(abs(move)-1):
            arr.append(arr.popleft())
            index.append(index.popleft())
        move = arr.popleft()
        ans.append(index.popleft())

    else:
        for _ in range(abs(move)-1):
            arr.appendleft(arr.pop())
            index.appendleft(index.pop())
        move = arr.pop()
        ans.append(index.pop())


print(*ans)