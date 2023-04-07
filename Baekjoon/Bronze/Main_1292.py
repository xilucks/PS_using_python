import sys


def input_data():
    start, end = map(int, sys.stdin.readline().split())

    return [start, end]


def solution():
    [start, end] = input_data()
    nums = []
    ans = 0

    for i in range(1_000):
        for j in range(i):
            nums.append(i)
            if len(nums) > end:
                return sum(nums[(start - 1):end])


print(solution())
