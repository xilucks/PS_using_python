import collections
import sys

N, P, Q = list(map(int, sys.stdin.readline().strip().split()))

dict = collections.defaultdict(int)

dict[0] = 1

def dp (i) :
    if dict[i] != 0 :
        return dict[i]
    dict[i] = dp(i//P)+ dp(i//Q)
    return dict[i]

print(dp(N))