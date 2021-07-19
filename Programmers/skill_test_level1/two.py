def solution(arr):
    min = 0
    for i in range(1, len(arr)):
        if arr[min] >= arr[i]:
            min = i
    del arr[min]
    if len(arr) == 0:
        arr.append(-1)
    return arr

print(solution([1,2,4,3,0]))