import sys

nums = list(map(int, sys.stdin.readline().strip().split()))
profit = 0
min_price = sys.maxsize

for price in nums:
    min_price = min(min_price,price)
    profit = max(profit, price - min_price)

print(profit)