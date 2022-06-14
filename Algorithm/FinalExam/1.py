num = [90, 82, 92, 75, 88, 80, 90, 90, 75]
dct = dict()
arr = []
for i in num:
    if not i in dct.keys():
        dct[i] = 1
        arr.append(i)
    else:
        dct[i] += 1

arr.sort()

for i in arr:
    print(i, dct[i])
