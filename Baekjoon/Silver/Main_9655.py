N = int(input())

SK = False
while True:
    if SK:
        SK = False
    else:
        SK = True

    if N >= 3:
        N -= 3
    else:
        N -= 1

    if N == 0:
        break

if SK:
    print('SK')
else:
    print('CY')
