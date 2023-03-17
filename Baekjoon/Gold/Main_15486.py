import sys

N = int(sys.stdin.readline())

schedules = []
checked = [0 for _ in range(N)]
answer = 0

for _ in range(N):
    schedules.append(list(map(int, sys.stdin.readline().strip().split())))

for index in range(N-1, -1, -1):
    schedule = schedules[index]
    [spend_time, money] = schedule

    if index == N - 1 or index + spend_time - 1 >= len(checked):
        if index + 1 == N and spend_time == 1:
            checked[index] = money
        elif index + 1 < N:
            checked[index] = checked[index + 1]

        continue

    today_progress = (checked[index + spend_time] + money) if index + spend_time < N else money
    if today_progress > checked[index + 1]:
        checked[index] = today_progress
    else:
        checked[index] = checked[index + 1]

print(checked[0])

