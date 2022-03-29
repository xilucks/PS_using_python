import collections
import sys

dict = collections.defaultdict(int)

N = int(input())
my = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
target = list(map(int, sys.stdin.readline().strip().split()))

ans = []

for card in my:
    dict[card] += 1

for card in target:
    num = dict.get(card)
    if num is None:
        num = 0
    ans.append(num)

print(*ans)
