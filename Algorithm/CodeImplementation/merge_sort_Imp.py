def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
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


# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list
    else:
        mid = len(my_list) // 2
        list1 = my_list[:mid]
        list2 = my_list[mid:]
        return merge(merge_sort(list1), merge_sort(list2))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))