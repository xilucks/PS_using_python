T = (80, 95, 80, 95, 77, 80)

while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    num = 0
    for i in range(len(T)):
        if T[i] == n:
            arr.append(i)
            num += 1

    print(arr, num)
