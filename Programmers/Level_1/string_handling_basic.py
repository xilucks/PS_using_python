def solution(s):
    for i in range(0, len(s)):

        if len(s) != 4 and len(s) != 6:
            return False

        if ord(s[i])>=48 and ord(s[i])<=57:
            answer = True
        else:
            return False


    return answer


s = input()

print(solution(s))