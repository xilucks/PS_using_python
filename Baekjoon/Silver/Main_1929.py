m, n = input().split(" ")
m, n = int(m), int(n)

arr = []
for i in range(n+1) :
        arr.append(i)

arr[0] = 0
arr[1] = 0
for i in range(2,n-1):
    j = 2
    if(i*j != 0):
        if i * j > n:
            break;
        while True:
            arr[i*j] = 0
            j += 1
            if i*j > n:
                break;

for i in range(m,len(arr)):
    if arr[i] != 0:
        print(arr[i])