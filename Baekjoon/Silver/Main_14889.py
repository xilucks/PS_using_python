import sys

N = int(sys.stdin.readline().strip())

board = []
visit = [False for _ in range(N)]


for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))


def dfs(member_num, index):
    global ans
    if member_num == N // 2:
        start_team, link_team = 0, 0

        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    start_team += board[i][j]
                elif not visit[i] and not visit[j]:
                    link_team += board[i][j]
        ans = min(ans, abs(start_team - link_team))

    else:
        for i in range(index, N):
            if not visit[i]:
                visit[i] = True
                dfs(member_num + 1, i)
                visit[i] = False


ans = int(1e9)
dfs(0, 0)

print(ans)