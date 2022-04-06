import collections
import sys

N = int(input())

nums = list(map(int, sys.stdin.readline().strip().split()))

nums_copy = list(sorted(set(nums)))

dic = {val: index for index, val in enumerate(nums_copy)}

for num in nums:
    print(dic[num], end= ' ')