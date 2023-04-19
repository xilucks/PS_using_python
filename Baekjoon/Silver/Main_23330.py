import sys


def input_data():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    return [N, nums]


def solution():
    [N, nums] = input_data()
    sorted_nums = sorted(nums)

    first_sum = 0

    for index in range(1, len(sorted_nums)):
        first_sum += abs(sorted_nums[index] - sorted_nums[0])

    sum_arr = [0 for _ in range(len(sorted_nums))]
    sum_arr[0] = first_sum
    for index in range(1, len(sorted_nums)):
        sum_arr[index] = sum_arr[index - 1] - (sorted_nums[index] - sorted_nums[index - 1]) * (len(sorted_nums) - index)

    print(sum(sum_arr) * 2)


solution()