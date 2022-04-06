import sys

n = int(input())

ground = list(map(int, sys.stdin.readline().strip().split()))

ground.sort(reverse= True)

ans = max(ground[0] * ground[1], ground[-1] * ground[-2])

print(ans)