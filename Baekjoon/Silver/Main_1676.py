num = int(input())

sum = 1
for i in range(1,num+1) :
    sum *= i

sum = str(sum)
# print(sum)
count = 0
for i in range(len(sum)-1,0,-1) :
    #print(i)
    if sum[i] == '0' :
        count += 1
    else :
        break;

print(count)