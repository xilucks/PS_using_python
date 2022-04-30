import sys

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    index = m
    tmp = list(map(int, sys.stdin.readline().split()))
    arr = tmp.copy()
    important = tmp.copy()

    important.sort(reverse=True)

    while True:
        if important[0] == arr[0]:
            if index == 0:
                ans = n - (len(arr)-1)
                break
            important.pop(0)
            arr.pop(0)
            m -= 1

        else:
            arr.append(arr.pop(0))

        index -= 1
        if index < 0:
            index = len(arr) - 1

    print(ans)

