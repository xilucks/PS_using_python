def solution(s):
    s = str(s)
    changer = ''
    answer = ''
    for i in range(len(s)):
        if ord(s[i])>=97 and ord(s[i]) <= 122:
            changer += s[i]

            if changer == 'zero':
                answer += '0'
                changer = ''

            elif changer == 'one':
                answer += '1'
                changer = ''

            elif changer == 'two':
                answer += '2'
                changer = ''

            elif changer == 'three':
                answer += '3'
                changer = ''

            elif changer == 'four':
                answer += '4'
                changer = ''

            elif changer == 'five':
                answer += '5'
                changer = ''

            elif changer == 'six':
                answer += '6'
                changer = ''

            elif changer == 'seven':
                answer += '7'
                changer = ''

            elif changer == 'eight':
                answer += '8'
                changer = ''

            elif changer == 'nine':
                answer += '9'
                changer = ''

            else:
                continue
        else:
            answer += s[i]

    answer = int(answer)
    return answer

print(solution('one4seveneight'))