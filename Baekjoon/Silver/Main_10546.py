import collections

n = int(input())

dct = collections.defaultdict(int)

for _ in range(n):
    name = input()
    dct[name] += 1

for _ in range(n-1):
    finish = input()
    dct[finish] -= 1

for name in dct.keys():
    if dct[name] > 0:
        print(name)
