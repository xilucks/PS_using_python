#중복문자제거
#중복된 문자를 제외하고 사전식 순서로 나열
import collections

str = input()

stack = []
counter = collections.Counter(str)
seen = set()
for i in str:
    counter[i] -= 1
    if i in seen:
        continue

    while stack and i <stack[-1] and counter[stack[-1]] > 0:
        seen.remove(stack.pop())

    stack.append(i)
    seen.add(i)

print(''.join(stack))