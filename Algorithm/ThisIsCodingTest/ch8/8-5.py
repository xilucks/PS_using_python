from typing import List

N, M = map(int, input().split())


d = [10001] * (M+1)

d[0] = 0

moneys = []

for i in range(N):
    moneys.append(int(input()))

for i in range(N):
    for j in range(moneys[i], M+1):
        if d[j - moneys[i]] != 10001:
            d[j] = min(d[j], d[j-moneys[i]] + 1)


print(d)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
