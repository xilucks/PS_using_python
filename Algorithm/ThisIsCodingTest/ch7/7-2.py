# 197p 부품찾기
import sys

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

M = int(input())

orders = list(map(int, sys.stdin.readline().split()))


def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return False


for order in orders:
    ans = search(arr, order, 0, len(arr)-1)

    if ans:
        print("yes", end=' ')
    else:
        print("no", end=' ')