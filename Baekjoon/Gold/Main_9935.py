
str = input()
boom = input()
boom_state = 0
main_stack = []

for i in range(len(str)):
    main_stack.append(str[i])
    if str[i] == boom[boom_state]:
        boom_state += 1

    else:
        boom_state -= 1
        if boom_state < 0:
            boom_state = 0

    if boom_state == len(boom) and str[i] == boom[-1]:
        for i in range(len(boom)):
            main_stack.pop()
            boom_state -= 1

print(main_stack)


