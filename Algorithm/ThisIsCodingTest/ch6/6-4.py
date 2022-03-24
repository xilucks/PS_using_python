# 182p, 두 배열의 원소 교체

N, K = map(int, input().split())

arr = []

for _ in range(2):
    arr.append(list(map(int, input().split())))

arr[0].sort()
arr[1].sort(reverse=True)

for i in range(K):
    if arr[0][i] < arr[1][i]:
        arr[0][i], arr[1][i] = arr[1][i], arr[0][i]


ans = sum(arr[0])

print(ans)
