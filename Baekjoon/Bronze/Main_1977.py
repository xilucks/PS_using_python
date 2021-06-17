m = int(input())
n = int(input())
count = 0
sum = 0
i = 1
while i**2 <= n :
    if(i**2 >= m and i**2 <= n) :
        count += 1
        sum += i**2
        if (count == 1):
            min = i ** 2


    i += 1

if(count == 0) :
    sum = -1

print(sum)
if( count>0 ):
    print(min)