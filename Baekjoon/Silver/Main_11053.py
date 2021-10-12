import sys

N = int(input())

nums = list(map(int,sys.stdin.readline().strip().split()))
arr = [1] * len(nums)
store = []

for i in range(len(nums)):
    if i == 0 :
        arr[i] = 1
    else:
        for j in range(0,i):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i],arr[j]+1)

ans = max(arr)
print(ans)
