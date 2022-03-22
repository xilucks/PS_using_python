#my solution
import sys

N, K = map(int, input().split())

ans = 0
while N != 1:
    if N%K == 0:
        N = N//K
    else :
        N -= 1

    ans += 1

print(ans)

#Greedy solution
N, K = map(int, input().split())

ans = 0

while True:
    target = (N//K) * K
    ans += (N-target)
    n = target

    if N < K:
        break
    ans += 1
    N //= K

ans += (N-1)
print(ans)
