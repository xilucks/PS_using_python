from math import comb

case = int(input())

# def judge(m, n):
#     if m == n :
#         return 1
#     elif m == 1:
#         return n
#     else:
#         return judge(m-1,n)+judge(m,n-1)

for i in range(case):

    m,n = input().split(" ")
    m = int(m)
    n = int(n)
    print(comb(n,m))
