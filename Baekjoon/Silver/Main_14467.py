cow=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
count = 0
num = int(input())
for i in range(num) :
    cownum, place = input().split(" ")
    if cow[int(cownum)-1] == -1 :
        cow[int(cownum) - 1] = int(place)
    elif cow[int(cownum)-1] != int(place) :
        count +=1
        cow[int(cownum)-1] = int(place)
    else :
        continue

print(count)