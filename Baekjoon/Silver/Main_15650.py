import sys

N, M = map(int, sys.stdin.readline().split())

ans = [] #정답을 담는 배열
arr = [0 for _ in range(M)] #정답에 넣기 전 숫자 배열을 담는 배열
visit = [False for _ in range(N+1)] # 방문처리를 위한 배열

def dfs(idx : int, num : int):
    if idx == M+1:
        ans.append(arr.copy())
        return

    for i in range(num, N+1):
        if not visit[i]:
            arr[idx-1] = i
            dfs(idx + 1, i + 1)
            arr[idx-1] = 0


def result():
    for value in ans:
        print(*value)

dfs(1, 1)
result()