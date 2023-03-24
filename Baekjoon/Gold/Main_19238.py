import collections
import sys

length, user_num, oil = map(int, sys.stdin.readline().strip().split())

road = []
visit = []
count = 0
last_oil = oil
working = False

for _ in range(length):
    road.append(list(map(int, sys.stdin.readline().strip().split())))
    visit.append([0] * length)

start_y, start_x = map(int, sys.stdin.readline().strip().split())
start_y, start_x = start_y - 1, start_x - 1
user_list = collections.defaultdict(list)

for _ in range(user_num):
    user_start_y, user_start_x, user_end_y, user_end_x = map(int, sys.stdin.readline().split())
    user_list[user_start_y - 1, user_start_x - 1] = [user_end_y - 1, user_end_x - 1]

bfs_queue = []
moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]
bfs_queue.append([0, start_y, start_x])
visit[start_y][start_x] = 1


def reset_bfs(y, x, queue):
    queue.clear()
    queue.append([0, y, x])
    visit.clear()
    for _ in range(length):
        visit.append([0] * length)

    visit[y][x] = 1


while bfs_queue:
    bfs_queue.sort()
    move, now_y, now_x = bfs_queue.pop(0)

    if not working and (now_y, now_x) in list(user_list.keys()):
        reset_bfs(now_y, now_x, bfs_queue)
        start_y, start_x = now_y, now_x
        count = 0
        working = True

    if last_oil < 0:
        last_oil = -1
        break

    for move in moves:
        dy, dx = move
        ny, nx = now_y + dy, now_x + dx

        if ny < 0 or ny >= length or nx < 0 or nx >= length or road[ny][nx] == 1:
            continue

        # 일을 하고 있는 상태
        if working and user_list[start_y, start_x] == [ny, nx]:
            user_list.pop((start_y, start_x))
            count += visit[now_y][now_x]
            last_oil -= count
            if last_oil < 0:
                last_oil = -1
                break
            else:
                last_oil += count * 2
            reset_bfs(ny, nx, bfs_queue)
            working = False
            break

        # 일을 안하고 있는 상태에서 현재 index가 유저가 있는 부분일 때
        elif not working and (ny, nx) in list(user_list.keys()):
            last_oil -= visit[now_y][now_x]
            reset_bfs(ny, nx, bfs_queue)
            count = 0
            start_y, start_x = ny, nx
            working = True
            break

        # 일을 안하고 있는 상태에서 탐색
        elif visit[ny][nx] == 0 and road[ny][nx] == 0:
            visit[ny][nx] = visit[now_y][now_x] + 1
            bfs_queue.append([visit[ny][nx], ny, nx])


if list(user_list):
    last_oil = -1
print(last_oil)
