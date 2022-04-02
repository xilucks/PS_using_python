import sys
from collections import deque

T = int(input())

for _ in range(T):
    visit = [0] * 10000
    queue = deque()
    start, target = map(int, sys.stdin.readline().strip().split())
    ans = ''
    queue.append([start, ans])

    while True:
        start, ans = queue.popleft()

        if start == target:
            break
        # D
        case1 = (start * 2) % 10000
        if not visit[case1]:
            visit[case1] = True
            queue.append([case1, ans + 'D'])

        #S
        case2 = start - 1

        if case2 == -1:
            case2 = 9999
        if not visit[case2]:
            visit[case2] = True
            queue.append([case2, ans + 'S'])

        #L
        case3 = (start * 10) % 10000 + (start//1000)

        if not visit[case3]:
            visit[case3] = True
            queue.append([case3, ans + 'L'])

        #R
        case4 = (start//10) + ((start % 10) * 1000)

        if not visit[case4]:
            visit[case4] = True
            queue.append([case4, ans + 'R'])

    print(ans)