def consecutive_sum(start, end):
    mid = (start+end)//2
    if start == end:
        return start
    else :
        return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)


# 테스트
print(consecutive_sum(1, 10))
