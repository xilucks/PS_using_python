n = int(input())
string = input()

not_chi = 0
for ch in string:
    if ch != 'C':
        not_chi += 1

div = not_chi + 1

if (n - not_chi) % div == 0:
    print((n - not_chi) // div)

else:
    print((n - not_chi) // div + 1)

