import sys


def solution():
    string = sys.stdin.readline()
    is_tag = False
    one_sentence = []
    ans = ''

    for index, spelling in enumerate(string):
        one_sentence.append(spelling)

        if spelling == '<':
            one_sentence.pop()
            while one_sentence:
                ans += one_sentence.pop()

            one_sentence = [spelling]
            is_tag = True
            continue

        if is_tag:
            if spelling == '>':
                ans += "".join(one_sentence)
                one_sentence = []
                is_tag = False
                continue

        else:
            if spelling == ' ' or index == len(string) - 1:
                one_sentence.pop()

                while one_sentence:
                    ans += one_sentence.pop()
                ans += " "
                one_sentence = []

    print(ans)


solution()