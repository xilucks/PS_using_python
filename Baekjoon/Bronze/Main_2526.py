import sys

multiple_num, div_num = map(int, sys.stdin.readline().split())

now_num = multiple_num
num_list = [now_num]
start_index = 0

while True:
    now_num *= multiple_num
    now_num %= div_num

    if now_num in num_list:
        num_list.append(now_num)
        break
    num_list.append(now_num)

for i in range(len(num_list)):
    if num_list[-1] == num_list[i]:
        start_index = i
        break

print(len(num_list) - 1 - start_index)

