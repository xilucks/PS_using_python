import math
import sys


def input_data():
    n, m = map(int, sys.stdin.readline().split())
    elevator = []

    for _ in range(m):
        elevator.append(list(map(int, sys.stdin.readline().split())))

    return [n, m, elevator]


def calculate_floor(before_total, total_count, low, top, up_floor, down_floor):
    if low > top:
        return before_total

    up_count = math.floor(low + (top - low) / 2)
    down_count = total_count - up_count

    total_floor = up_floor * up_count - down_floor * down_count

    if total_floor > 0:
        return calculate_floor(total_floor, total_count, low, up_count - 1, up_floor, down_floor)

    else:
        return calculate_floor(before_total, total_count, up_count + 1, top, up_floor, down_floor)


def solution():
    [n, m, elevator_list] = input_data()

    ans = int(1e9)

    for elevator in elevator_list:
        up_floor, down_floor = elevator

        move = calculate_floor(int(1e9), n, 0, n, up_floor, down_floor)
        ans = move if ans > move > 0 else ans

    print(ans)


solution()


