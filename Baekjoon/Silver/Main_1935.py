import sys

N = int(input())
str = sys.stdin.readline()
arr = []
stack = []
ans = 0

for _ in range(N):
    arr.append(int(input()))

for ch in str:
    if 65 <= ord(ch) <= 90:
        stack.append(arr[ord(ch)-65])

    else:
        if ch == '*':
            b, a = stack.pop(), stack.pop()
            tmp = a * b
            stack.append(tmp)

        if ch == '/':
            b, a = stack.pop(), stack.pop()
            tmp = a / b
            stack.append(tmp)

        if ch == '+':
            b, a = stack.pop(), stack.pop()
            tmp = a + b
            stack.append(tmp)

        if ch == '-':
            b, a = stack.pop(), stack.pop()
            tmp = a - b
            stack.append(tmp)

print('{:.2f}'.format(stack.pop()))