import collections
import sys

hm = collections.defaultdict(int)

n, m = map(int, input().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))


for i in a:
    hm[i] += 1
for j in b:
    hm[j] += 1

count = 0
for v in hm.keys():
    if hm[v] > 1:
        count += 1

print(len(a) - count + len(b) - count)