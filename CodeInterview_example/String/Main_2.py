import sys

strs = list(map(int,sys.stdin.readline().strip().split()))

def solve(self, s: strs) -> None :
    left, right = 0, len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1

def solve_2(self, s:strs) -> None:
    s.reverse()
