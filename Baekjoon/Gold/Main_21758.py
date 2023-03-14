import sys

N = sys.stdin.readline().strip()
honeys = list(map(int, sys.stdin.readline().split(' ')))
honey_sum = list(map(int, [0] * len(honeys)))
honey_sum[0] = honeys[0]

for index in range(1, len(honey_sum)):
    honey_sum[index] = honeys[index] + honey_sum[index - 1]


def honey_dp(index):
    if honey_sum[index] == 0:
        honey_sum[index] = honeys[index] + honey_dp(index - 1)
        return honey_sum[index]

    else:
        return honey_sum[index]


def right_honey_position(honey_arr):
    maximum_honey = 0
    for index, second_bee_position in enumerate(honey_arr):
        if index == 0:
            continue
        first_bee = honey_dp(len(honeys) - 1) - second_bee_position - honeys[0]
        second_bee = honey_dp(len(honeys) - 1) - honey_dp(index)

        if first_bee + second_bee > maximum_honey:
            maximum_honey = first_bee + second_bee

    return maximum_honey


def left_honey_position(honey_arr):
    maximum_honey = 0
    for index, second_bee_position in enumerate(honey_arr):
        if index == 0 or index == len(honeys) - 1:
            continue
        first_bee = honey_dp(len(honeys) - 1) - second_bee_position - honeys[len(honeys) - 1]
        second_bee = honey_dp(index) - second_bee_position
        if first_bee + second_bee > maximum_honey:
            maximum_honey = first_bee + second_bee

    return maximum_honey


def middle_honey_position(honey_arr):
    maximum_honey = 0
    for index, middle_honey_position in enumerate(honey_arr):
        if index == 0 or index == len(honeys) - 1:
            continue
        first_bee = honey_dp(index) - honeys[0]
        second_bee = honey_dp(len(honeys) - 1) - honey_dp(index - 1) - honeys[len(honeys) - 1]
        if first_bee + second_bee > maximum_honey:
            maximum_honey = first_bee + second_bee

    return maximum_honey


print(max(right_honey_position(honeys), left_honey_position(honeys), middle_honey_position(honeys)))


