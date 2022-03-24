#178p 위에서 아래로

N = int(input())

arr = []
for _ in range(N):
    arr.append(input())

arr.sort(reverse=True)

print(arr)