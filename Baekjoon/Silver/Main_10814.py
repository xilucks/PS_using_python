import sys

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(str, sys.stdin.readline().split())))

arr.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(*arr[i])