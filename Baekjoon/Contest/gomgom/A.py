chicken = int(input())
c, b = map(int, input().split())

im_chi = c//2 + b

if im_chi > chicken:
    print(chicken)
else:
    print(im_chi)