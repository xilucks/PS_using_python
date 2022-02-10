import sys

count = 0
result = 0

N, M, K = map(int, sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().strip().split()))

nums.sort(reverse=True)

while count != M :
    for i in range(K):
        result += nums[0]
        count += 1
        if count == M:
            break
    result += nums[1]
    count += 1

print(result)


#develop ver.
count = 0
result = 0


count = int(M / (K+1)) * K
count += M % (K+1)

result += nums[0] * count
result += nums[1] * (M-count)

print(result)