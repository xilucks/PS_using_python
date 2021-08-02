import sys

m, n = input().split(" ")
m = int(m)
n = int(n)

arr = [[0 for col in range(n)] for row in range(m)]

for i in range(m) :
    str = sys.stdin.readline()
    for j in range(n):
        arr[i][j] = str[j]

y, x = input().split();
y = int(y);
x = int(x);

xc = 0;
yc = 0;

for i in range(m):
    yc += 1
    xc = 0
    for j in range(n):
        xc += 1
        if (xc == x and yc == y):
            if arr[i][j] == '#':
                print('.', end='')
            else:
                print('#', end='')
        else:
            print(arr[i][j], end='')

    for J in range(n-1, -1, -1):
        xc += 1
        if (xc == x and yc == y):
            if arr[i][J] == '#':
                print('.', end='')
            else:
                print('#', end='')
        else:
            print(arr[i][J], end='')
    print("")

for I in range(m-1, -1 ,-1):
    yc += 1
    xc = 0
    for j in range(n):
        xc += 1
        if (xc == x and yc == y):
            if arr[I][j] == '#':
                print('.', end='')
            else:
                print('#', end='')
        else:
            print(arr[I][j], end='')
    for J in range(n - 1, -1, -1):
        xc += 1
        if (xc == x and yc == y):
            if arr[I][J] == '#':
                print('.', end='')
            else:
                print('#', end='')
        else:
            print(arr[I][J], end='')
    print("")
