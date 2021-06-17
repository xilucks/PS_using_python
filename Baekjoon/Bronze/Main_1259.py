def is_palindrome(word):
    # 코드를 입력하세요.
    list_word = list(word)
    reversed_list = list_word[::-1]

    return list_word == reversed_list
count = 0
a = str(input())
while a != '0' :
    if(is_palindrome(a) == True) :
        print('yes')
    else :
        print('no')

    a = input()