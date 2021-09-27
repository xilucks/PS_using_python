import sys

X = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

index = 0
stack = [0]*1000000

for ch in X :
    stack[index] = ch
    index += 1
    if index >= len(boom) :
        chk = True
        for i in range(len(boom)) :
            if stack[index - len(boom) + i] != boom[i]:
                chk = False
                break

        if chk:
            index -= len(boom)

if index == 0 :
    print("FRULA")
else:
    for i in range(index):
        print(stack[i], end ='')