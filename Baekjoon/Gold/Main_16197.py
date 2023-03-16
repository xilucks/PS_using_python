import collections
import sys

# set env
bfs_queue = collections.deque([])
coin_moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
coin_map = []
coin_index = []

N, M = map(int, sys.stdin.readline().strip().split())

for _ in range(N):
    map_line = sys.stdin.readline().strip()
    coin_map.append(list(map_line[i] for i in range(len(map_line))))


# set Start Coins
for y in range(N):
    for x in range(M):
        if coin_map[y][x] == 'o':
            coin_index.append([y, x])

    if len(coin_index) == 2:
        break


# Check Coin out
def check_out(y_index, x_index):
    if (y_index < 0 or y_index >= N) or (x_index < 0 or x_index >= M):
        return True
    return False


bfs_queue.append([1, coin_index[0], coin_index[1]])
out_count_list = []

# graph search
while bfs_queue:
    [count, first_coin_index, second_coin_index] = bfs_queue.popleft()

    if count > 10:
        break

    for move in coin_moves:
        [dy, dx] = move
        [first_coin_y, first_coin_x] = first_coin_index
        [second_coin_y, second_coin_x] = second_coin_index

        first_coin_ny = first_coin_y + dy
        first_coin_nx = first_coin_x + dx

        second_coin_ny = second_coin_y + dy
        second_coin_nx = second_coin_x + dx

        if check_out(first_coin_ny, first_coin_nx) and check_out(second_coin_ny, second_coin_nx):
            continue

        elif check_out(first_coin_ny, first_coin_nx) ^ check_out(second_coin_ny, second_coin_nx):
            out_count_list.append(count)
            continue

        else:
            if coin_map[first_coin_ny][first_coin_nx] == '#':
                first_coin_ny, first_coin_nx = first_coin_y, first_coin_x
            if coin_map[second_coin_ny][second_coin_nx] == '#':
                second_coin_ny, second_coin_nx = second_coin_y, second_coin_x
            bfs_queue.append([count + 1, [first_coin_ny, first_coin_nx], [second_coin_ny, second_coin_nx]])


print(min(out_count_list) if out_count_list else -1)

