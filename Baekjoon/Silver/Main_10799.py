string = input()
stack = []

stick = 0
laser = True
ans = 0
i = 0
for ch in string:
    if ch == '(':
        stack.append(ch)
        stick += 1
        laser = False

    else:
        stack.pop()
        stick -= 1
        if laser:
            ans += 1

        else:
            ans += stick
            laser = True

print(ans)