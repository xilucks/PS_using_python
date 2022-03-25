# 201p 떡볶이 떡 만들기
import sys

N, M = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()


def cut(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        length = 0

        for rice_cake in arr:
            if rice_cake > arr[mid]:
                length += rice_cake - arr[mid]

            else:
                continue

        if length == M:
            return arr[mid]

        elif length < M:
            end = mid - 1

        else:
            start = mid + 1

    return arr[(start + end) // 2]


print(cut(arr, M, 0, len(arr) - 1))
