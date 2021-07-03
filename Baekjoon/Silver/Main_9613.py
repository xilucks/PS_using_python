import sys

t = int(input())
for k in range(0,t,1):
    result = 0
    nums = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1,nums[0],1):
        for j in range(i+1,nums[0]+1,1):
            if(nums[i] > nums[j]) :
                a = nums[i]
                b = nums[j]
            else :
                a = nums[j]
                b = nums[i]
            while b != 0:
                n = a%b
                if n == 0:
                    result += b
                    break;
                else :
                    a = b
                    b = n

    print(result)