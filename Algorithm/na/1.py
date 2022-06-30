keyboard = ['a', 'b'], ['c', 'd'], ['e', 'f']
seek = False

def solution(word):
    count = 0
    before_y = 0
    before_x = 0
    y_index = 0
    x_index = 0
    s = 0

    for ch in word:
        len_sum = 10000
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                if keyboard[i][j] == ch:
                    tmp = abs(i - before_y) + abs(j - before_x)
                    print('tmp',tmp)
                    print(j, before_y, i, before_x)
                    print('--')

                    if tmp < len_sum:
                        len_sum = tmp
                        y_index = i
                        x_index = j

                    if count == 0:
                        len_sum = 0
                        y_index = i
                        x_index = j

        if len_sum == 10000:
            s += 20
        else:
            s += len_sum
            count += 1
            before_y = y_index
            before_x = x_index

        print(len_sum)
        print(before_y, before_x)
        print(s,count)

    return [s,count]

word = 'abcd'
print(solution(word))