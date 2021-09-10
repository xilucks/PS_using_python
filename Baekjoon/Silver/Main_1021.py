import sys
from collections import deque

N, M = input().split()
N, M = int(N), int(M)

ans = 0

deq = deque()
for i in range(1,N+1) :
    deq.append(i)

nums = list(map(int, sys.stdin.readline().strip().split()))

for i in nums:
    if i == deq[0]:
        deq.popleft()
    else:
        l = 0
        r = 0
        while deq[l] != i:
            l += 1
        while deq[r] != i:
            r -= 1
        if l > abs(r):
            ans += abs(r)
            for i in range(abs(r)) :
                deq.appendleft(deq.pop())
        else :
            ans += l
            for i in range(l) :
                deq.append(deq.popleft())
        deq.popleft()

print(ans)
