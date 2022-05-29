from collections import deque

maze = ["AAAAA", "AABBB", "CAEFG", "AAEFF"]
queries = ["1 1 1 5 AF", "1 1 4 5 AF", "2 1 4 5 FAE", "1 5 4 5 ABF", "1 1 4 1 A"]

def solution(maze, queries):
    maze_y, maze_x = len(maze), len(maze[0])
    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
    ans = []

    for query in queries:
        visit = [[0] * maze_x for _ in range(maze_y)]
        q = deque([])
        start_y, start_x, end_y, end_x, command = query.split()
        start_y, start_x, end_y, end_x = int(start_y) - 1, int(start_x) - 1, int(end_y) - 1, int(end_x) - 1

        q.append([start_y, start_x])
        visit[start_y][start_x] = 1

        while q:
            tmp = q.popleft()
            y, x = tmp[0], tmp[1]

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny >= maze_y or nx >= maze_x or ny < 0 or nx < 0:
                    continue

                if not maze[ny][nx] in command:
                    continue

                if visit[ny][nx] != 0:
                    continue

                visit[ny][nx] = visit[y][x] + 1
                q.append([ny, nx])

        if visit[end_y][end_x] == 0:
            ans.append(-1)
        else:
            ans.append(visit[end_y][end_x])

    return ans

    # string = ''
    # string += '['
    #
    # for word in ans:
    #     word_str = str(word)
    #     string += word_str + ', '
    #
    # string = string[0: len(string)-2]
    # string +=']'
    # print(string)

solution(maze,queries)