def merge(list1, list2):
    ans = []
    while (len(list1) != 0) or (len(list2) != 0):
        if (len(list1) == 0):
            while len(list2) != 0:
                x = list2.pop(0)
                ans.append(x)
        elif (len(list2) == 0):
            while len(list1) != 0:
                x = list1.pop(0)
                ans.append(x)

        elif list1[0] >= list2[0]:
            x = list2.pop(0)
            ans.append(x)
        elif (list1[0] < list2[0]):
            x = list1.pop(0)
            ans.append(x)

    return ans


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))