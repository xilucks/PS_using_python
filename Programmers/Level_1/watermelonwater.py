import sys
sys.setrecursionlimit(10**8)

def solution(n):
    if n == 1:
        return '수'

    elif arr[n] != 0:
        return arr[n]
    else:
        if n%2 == 0:
            arr[n] = solution(n-1) +'박'
            return arr[n]
        else:
            arr[n] = solution(n-1)+'수'
            return arr[n]


arr = [0]*10001
print(solution(3))