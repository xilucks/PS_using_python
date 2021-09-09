import sys
from collections import deque

a = int(input())
queue = deque()

for i in range(a):
    text = list(map(str, sys.stdin.readline().strip().split()))

    if text[0] == 'push_front':
        queue.appendleft(text[1])

    elif text[0] == 'push_back':
        queue.append(text[1])

    elif text[0] == 'pop_front':
        if len(queue) != 0:
            print(queue.popleft())
        else :
            print(-1)

    elif text[0] == 'pop_back':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)

    elif text[0] == 'size':
        print(len(queue))

    elif text[0] == 'empty':
        if(len(queue) == 0) :
            print(1)
        else:
            print(0)

    elif text[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)


    elif text[0] == 'back':
        if len(queue) != 0:
            print(queue[len(queue) - 1])
        else:
            print(-1)