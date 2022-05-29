balance = [30, 30, 30, 30]
transaction = [[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]]
abnormal = [1]

# 아이디어, balance // abnormal// over_abnormal

def solution(balance, transaction, abnormal):
    abnormal_stock = [[0] * len(balance)]
    over_abnormal = [[0] * len(balance)]
    abnormal_stock[abnormal-1] = balance[abnormal-1]
    balance[abnormal-1] = 0

    for tmp in transaction:
        start = tmp[0]
        target = tmp[1]
        value = tmp[2]
        #
        # if abnormal_stock[start] != 0:
        #     if over_abnormal[start] > value:




