import collections
import sys

N = int(sys.stdin.readline())

first = list(map(int, sys.stdin.readline().split()))
second = []
third = []
nums = sorted(first.copy())
numbers_dict = collections.defaultdict(int)
count = 0
move_history = []

for index in nums:
    numbers_dict[index] = 1


while len(third) != N:
    top_num = nums.pop()
    position = numbers_dict[top_num]

    moving_num = 0
    while moving_num != top_num:
        count += 1
        if position == 1:
            moving_num = first.pop()
            if moving_num == top_num:
                third.append(moving_num)
                numbers_dict[moving_num] = 3
                move_history.append(['1', '3'])
            else:
                second.append(moving_num)
                numbers_dict[moving_num] = 2
                move_history.append(['1', '2'])

        elif position == 2:
            moving_num = second.pop()
            if moving_num == top_num:
                third.append(moving_num)
                numbers_dict[moving_num] = 3
                move_history.append(['2', '3'])
            else:
                first.append(moving_num)
                numbers_dict[moving_num] = 1
                move_history.append(['2', '1'])

print(count)
for history in move_history:
    print(" ".join(history))