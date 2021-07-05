import sys

case = int(sys.stdin.readline())

for i in range(0, case) :
    arr = [0, 0]
    num = int(sys.stdin.readline())

    for j in range(0, num-1) :
        arr.append(1)
    for k in range(2, num-1):
        index = 2
        while True:
            if k*index > num:
                break

            arr[k*index] = 0
            index += 1

    while num != 1:
        for n in range(len(arr)) :
            if arr[n] == 1:
                if num%n == 0:
                    while num%n == 0:
                        arr[n] += 1
                        num = num // n
                else:
                    arr[n] = 0

    for result in range(len(arr)):
        if arr[result] > 1:
            print(result, (arr[result]-1))
