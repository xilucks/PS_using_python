import collections
import sys

N, L = map(int, sys.stdin.readline().split())

sign_info = collections.deque()

for _ in range(N):
    sign_info.append(list(map(int, sys.stdin.readline().split())))

now_distance = 0
time = 0
position, red_time, blue_time = -1, 0, 0
isBlue = False

while now_distance != L:
    time += 1

    if sign_info and position < now_distance:
        position, max_red_time, max_blue_time = sign_info.popleft()
        blue_time, red_time = max_blue_time, max_red_time

    if time % (max_red_time + max_blue_time) - red_time >= 0:
        isBlue = True
    else:
        isBlue = False

    if now_distance != position:
        now_distance += 1

    else:
        if isBlue:
            now_distance += 1


print(time + 1)


