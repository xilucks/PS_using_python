import sys
from queue import PriorityQueue

input = sys.stdin.readline
pq = PriorityQueue()

n = int(input())

for i in range(n):
    x = int(input())
    if x != 0:
        pq.put(x)

    else:
        if pq.empty():
            print(0)
        else:
            print(pq.get())