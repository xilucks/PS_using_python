import sys


def input_data():
    mask = list(map(int, sys.stdin.readline().split()))
    shirt = list(map(int, sys.stdin.readline().split()))
    pants = list(map(int, sys.stdin.readline().split()))

    return [mask, shirt, pants]


def solution():
    [mask, shirt, pants] = input_data()

    white_mask, black_mask = mask
    white_shirt, black_shirt = shirt
    white_pants, black_pants = pants

    white_set = min(white_mask, black_shirt, white_pants)
    black_set = min(black_mask, white_shirt, black_pants)

    ans = min(black_set, white_set) * 2 if white_set == black_set else min(black_set, white_set) * 2 + 1

    print(ans)


solution()