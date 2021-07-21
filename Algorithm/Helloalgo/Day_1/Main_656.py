m, n = input().split()
num,room = int(m),int(n)

num0, num1, num2, num3, num4 = 0,0,0,0,0
for i in range(num):
    s,y = input().split()
    s = int(s)
    y = int(y)
    if y == 1 or y == 2:
        num0 += 1
    elif s == 0:
        if y == 3 or y == 4:
            num1 += 1
        else:
            num3 += 1
    else:
        if y == 3 or y == 4:
            num2 += 1
        else:
            num4 += 1

roomcount = 0

#print(num0, num1, num2, num3, num4)
roomcount += int(num0/room)
if num0%room != 0 :
    roomcount += 1

roomcount += int(num1/room)
if num1%room != 0 :
    roomcount += 1

roomcount += int(num2/room)
if num2%room != 0 :
    roomcount += 1

roomcount += int(num3/room)
if num3%room != 0 :
    roomcount += 1

roomcount += int(num4/room)
if num4%room != 0 :
    roomcount += 1

print(int(roomcount))