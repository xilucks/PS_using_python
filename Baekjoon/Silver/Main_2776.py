import collections
import sys

tc = int(input())

for i in range(tc):
    dct = collections.defaultdict(int)

    my_num = int(input())
    tmp_memory = list(map(int, sys.stdin.readline().split()))

    for ch in tmp_memory:
        dct[ch] = 1

    your_num = int(input())
    tmp_memory = list(map(int, sys.stdin.readline().split()))

    for word in tmp_memory:
        print(dct[word])
