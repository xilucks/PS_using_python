def fin(a):
    if a == 1 or a == 2:
        return 1
    else:
        return fin(a-2) + fin(a -1)

print(fin(3))

for i in range(3) :
    print(i)

