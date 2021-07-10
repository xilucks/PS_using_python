nums = int(input())

sum = 0

one_two = 0
three_four = 0
one_four = 0

pizza = 0

for i in range(nums):
    m,n = input().split('/')
    m,n = int(m), int(n)

    if m == 1 and n == 2:
        one_two += 1


    elif m == 1 and n == 4:
        one_four += 1


    else:
        three_four+= 1

pizza += one_two//2
one_two %= 2

if one_four > three_four:
    pizza += three_four
    one_four, three_four = one_four-three_four, 0

elif one_four <= three_four:
    pizza += one_four
    three_four, one_four = three_four-one_four, 0

pizza += one_four//4
one_four %= 4

while True:
    if one_four ==0 or one_two == 0:
        break;
    elif one_four == 1:
        pizza += 1
        one_four -= 1
        one_two -= 1
    elif one_four == 2:
        pizza +=1
        one_four -= 2
        one_two -= 1
    else:
        pizza += 1
        one_four -= 2
        one_two -= 1

if(one_four < 4 and one_four>0):
    pizza +=1
    one_four = 0

print(pizza + three_four + one_two + one_four)