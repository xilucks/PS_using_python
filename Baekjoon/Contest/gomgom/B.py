import collections

dct = collections.defaultdict(int)
n = int(input())
ans = 0

for _ in range(n):
    string = input()

    if string == 'ENTER':
        dct.clear()

    else:
        if dct[string] == 0:
            ans += 1
            dct[string] += 1

print(ans)


