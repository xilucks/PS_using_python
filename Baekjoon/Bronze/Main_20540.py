import sys


def input_data():
    return sys.stdin.readline().strip()


def solution():
    mbti = input_data()
    answer = []

    for spelling in mbti:
        if spelling == 'I':
            answer.append('E')
        elif spelling == 'E':
            answer.append('I')

        elif spelling == 'S':
            answer.append('N')
        elif spelling == 'N':
            answer.append('S')

        elif spelling == 'T':
            answer.append('F')
        elif spelling == 'F':
            answer.append('T')

        elif spelling == 'P':
            answer.append('J')
        elif spelling == 'J':
            answer.append('P')

    return "".join(answer)


print(solution())

