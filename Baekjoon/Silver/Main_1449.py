import collections
import sys


def input_data():
    N, L = map(int, sys.stdin.readline().split())
    hole_info = sorted(list(map(int, sys.stdin.readline().split())))
    location = collections.deque(hole_info)

    return [N, L, location]


def solution():
    N, L, location = input_data()
    count = 0

    while location:
        count += 1
        left = location.popleft()
        right = 0

        if location:
            count += 1
            right = location.pop()

        if right != 0 and left + L > right:
            count -= 1
            right = 0

        while location and left + L > location[0]:
            location.popleft()

        while location and right != 0 and right - L < location[len(location) - 1]:
            location.pop()

    print(count)


solution()