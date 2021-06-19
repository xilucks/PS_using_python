x = int(input())
count = 0
stick = 64
total = 0

while x != total and x <=64 :
    if x < stick :
        stick /= 2
    elif stick + total > x :
        stick /= 2
    else :
        total += stick
        count += 1

print(count)

