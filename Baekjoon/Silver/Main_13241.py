
def gcd(m,n):
    if n > m:
        a = n
        b = m
    else:
        a = m
        b = n
    while b > 0:
        a,b = b, a%b
    return a


m,n = input().split(" ")
m = int(m)
n = int(n)
print(m*n//gcd(m,n))