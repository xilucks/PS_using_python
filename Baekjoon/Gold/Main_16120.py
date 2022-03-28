string = input()

stack = []
p_count = 0
PPAP_num = 0
PPA = False

ans = "NP"

for str in string:

    if str == 'P':
        if PPA:
            for _ in range(3):
                stack.pop()
            p_count -= 2
            PPAP_num += 1
        PPA = False
        p_count += 1

    if str == 'A':
        if not stack:
            ans = 'NP'
            PPA = False

        elif p_count > 1 and stack[-1] == 'P':
            PPA = True

        elif stack[-1] == 'A':
            PPA = False

    stack.append(str)

if len(stack) == 1 and stack[0] == 'P':
    ans = "PPAP"


print(ans)
