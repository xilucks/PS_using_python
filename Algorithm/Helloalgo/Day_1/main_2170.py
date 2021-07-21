n = int(input())
str = input()
index = str.index('*')  #1
answer = ''
for i in range(n):
    str2 = input()
    length = len(str)-(index+1)
    if str[0:index] == str2[0:index] :
        answer = 'DA'
        str2= str2[index:]
        if str[-length:] == str2[-length:]:
            answer = 'DA'
        else:
            answer = 'NE'

    else :
        answer = "NE"
    print(answer)
