import re
from collections import deque

T = int(input())

for i in range(T):
    str = input()
    N = int(input())
    N, M = input()
    nums = re.sub('[^0-9]',' ',nums)
    if N == 0 : deq = deque()
    else : deq = deque(map(int, nums.strip().split(' ')))
    state = True
    error = False

    for i in str:
        if i == 'R':
            if state == True:
                state = False
            else:
                state = True
        if i == 'D':
            if not deq:
                error = True
                break
            else:
                if state == True:
                    deq.popleft()
                else:
                    deq.pop()

    if state == False:
        deq.reverse()


    if error == True:
        print('error')
    else :
        if len(deq) == 0 :
            print('[]')
        else :
            deq = list(deq)
            print('[', end='')
            for i in range(len(deq) - 1):
                print(deq[i], end=",")
            print(deq[len(deq) - 1], end='')
            print(']')