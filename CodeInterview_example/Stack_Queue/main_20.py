str = input()

stack = []

table = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
}

state = True
for char in str:
    if char not in table :
        stack.append(char)
    elif not stack or table[char] != stack.pop():
        state = False
        break

if stack :
    state = False

print(state)

