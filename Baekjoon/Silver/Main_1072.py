import math

x,y = input().split();
x,y = int(x),int(y)

z = math.trunc((100*y/x))

l = -1
r = 1000000000

while l < r:
    mid = (l+r+1)//2
    tmpx = x+mid
    tmpy = y+mid
    tmpz = math.trunc(100*tmpy/tmpx)

    if tmpz > z:
        r = mid-1
    else :
        l = mid

if z >= 99:
    print(-1)
else:
    print(l+1)