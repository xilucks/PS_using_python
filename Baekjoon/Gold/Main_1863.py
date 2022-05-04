N = int(input())

stack = []
ans = 0

for i in range(N):
    x, y = map(int, input().split())

    if not stack or stack[-1] < y:
        stack.append(y)
    else:
        while stack and stack[-1] > y:
            stack.pop()
            ans += 1

        if not stack or stack[-1] < y:
            stack.append(y)

    if stack[-1] == 0:
        stack.pop()


if stack:
    ans += len(stack)

print(ans)
