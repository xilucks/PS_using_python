N = int(input())

arr = [[]for _ in range(N+2)]

arr[1] = 1
arr[2] = 3

for i in range(3, N+1):
    arr[i] = (arr[i-1] + arr[i-2]*2)

print(arr[N] % 10007)