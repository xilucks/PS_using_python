import sys


def input_data():
    N, L = map(int, sys.stdin.readline().split(' '))
    hole_info = []

    for _ in range(N):
        hole_info.append(list(map(int, sys.stdin.readline().split())))

    return [N, L, hole_info]


def solution():
    [N, L, hole_info] = input_data()
    hole_info.sort()

    hole_cover = 0
    ans = 0

    for hole in hole_info:
        [hole_start, hole_end] = hole
        hole_end -= 1

        while True:
            if hole_cover >= hole_end:
                break

            elif hole_start > hole_cover:
                hole_cover = hole_start - 1
                ans += 1
                hole_cover += L

            else:
                ans += 1
                hole_cover += L

    print(ans)


solution()