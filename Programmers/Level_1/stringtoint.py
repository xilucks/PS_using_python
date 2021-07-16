def solution(s):
    s = str(s)
    if s[0] == '-' :
        s = int(s[1:])
        s *= -1
    elif s[0] =='+':
        s = int(s[1:])
    else :
        s = int(s)

    answer = s
    #타입 알아보기
    #print(type(s))
    return answer
#출력 확인
#print(solution(1234))