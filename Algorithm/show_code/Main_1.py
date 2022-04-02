# dfs

# 물약 개수
import sys

N = int(input())

potion = list(map(int, sys.stdin.readline().strip().split()))

print(potion)

discount = []

ans = (2**31-1)
for i in range(len(potion)):
    discount_num = int(input()) #i번째를 샀을 때 할인해주는 개수
    tmp = []
    for j in range(discount_num):
        potion_num, coin = map(int, input().split())
        tmp.append([potion_num, coin])
    discount.append(tmp)




def dfs(start, money, ans, count):
    print(money)
    print(potion_copy)
    print(visit)

    if count == len(potion)-1:
        ans = min(ans, money)
        return

    for tmp in discount[start-1]:
        index = tmp[0]
        discount_coin = tmp[1]

        potion_copy[index-1] -= discount_coin
        if potion_copy[index-1] < 1:
            potion_copy[index-1] = 1
    print(potion_copy)
    for tmp in discount[start - 1]:
        index = tmp[0]

        if not visit[index]:
            visit[index] = True
            money += potion_copy[index-1]
            count += 1
            dfs(index, money, ans, count)
            visit[index] = False
            count -= 1
            money -= potion_copy[index-1]


for i in range(1, len(potion)):
    potion_copy = potion.copy()
    visit = [False for _ in range(len(potion) + 1)]
    start = i
    money = 0
    count = 0

    visit[i] = True

    dfs(start, money, ans, count)

print(ans)




