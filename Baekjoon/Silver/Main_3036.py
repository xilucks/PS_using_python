import sys

n = int(input())
rings = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1,n,1):
    a = rings[0]
    b = rings[i]

    while b != 0:
        n = a%b

        if n == 0:
            print("{}/{}".format(rings[0]//b,rings[i]//b))
            break;

        else:
            a = b
            b = n