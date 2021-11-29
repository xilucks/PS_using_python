import collections
import sys

a = int(sys.stdin.readline())

dict = collections.defaultdict(int)
max = 0
for i in range(a):
    i = int(sys.stdin.readline())
    dict[i] += 1
    if i > max :
        max = i


for i in range(0,max+1):
    for j in range(dict[i]):
        print(i)
