from collections import defaultdict
import sys
input = sys.stdin.readline

dict = defaultdict(int)
count = 0

while True:
    name = input().rstrip()
    if not name:
        break
    dict[name] += 1
    count += 1

trees = list(sorted(dict.keys()))

for k in trees:
    print("%s %.4f" % (k, dict[k] * 100 / count))


