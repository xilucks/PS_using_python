#A를 B번 곱해서 C로 나눔

import sys

A, B, C = map(int,sys.stdin.readline().split())

def cal(A, B, C) :
    if B == 1 :
        return A%C
    else :
        tmp = cal(A, B//2, C)
        if B%2 == 0:
            return tmp*tmp%C
        else:
            return tmp*tmp*A%C

print(cal(A,B,C))