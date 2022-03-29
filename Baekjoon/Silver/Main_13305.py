import sys

N = int(input())

dist = list(map(int, sys.stdin.readline().strip().split()))
city = list(map(int, sys.stdin.readline().strip().split()))

best_city = 0
money = 0

for i in range(len(city)-1):
    if i == 0:
        money = dist[i] * city[0]
        best_city = city[i]

    else:
        if best_city > city[i]:
            best_city = city[i]
        money += dist[i] * best_city


print(money)