import sys

m, n = input().split(" ")
m = int(m)
n = int(n)

arr = [[0 for col in range(n)] for row in range(m)]

for i in range(m) :
    str = sys.stdin.readline()
    for j in range(n):
        arr[i][j] = str[j]

k = int(input())

for i in range(m):
    for I in range(k):
        for j in range(n):
            for J in range(k):
                print(arr[i][j], end='')
        print("")