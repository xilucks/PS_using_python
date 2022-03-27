N = int(input())

d = [0] * N

for i in range(1, N-1):
    if i == 1:
        d[i] = 1

    elif i == 2:
        d[i] = 3

    else:
        d[i] = d[i-1] + d[i-1] * 2

print(d[N])
