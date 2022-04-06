import sys

N, M = map(int, input().split())

arr = []
target = [0 for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            target[i] += 1

attack = []

for _ in range(2):
    start, end = map(int, input().split())
    for i in range(start-1, end):
        target[i] -= 1
        if target[i] < 0:
            target[i] = 0

ans = 0
for num in target:
    ans += num

print(ans)