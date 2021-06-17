sum = 0
i = 0
max = 0
while i < 4 :
    out,come = input().split()
    sum -= int(out)
    if sum < 0 :
        sum = 0
    sum += int(come)
    if sum > 10000 :
        sum = 10000
    if sum > max :
        max = sum
    i+=1

print(max)