import sys


def input_data():
    nums = []

    while True:
        first, second = map(int, sys.stdin.readline().split())
        if first == 0 and second == 0:
            return nums

        nums.append([first, second])


def solution():
    data = input_data()

    for num in data:
        if num[0] > num[1]:
            print('Yes')
        else:
            print('No')


solution()