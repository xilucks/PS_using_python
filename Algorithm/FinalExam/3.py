student = [1,2,3,4,5,6]
python = [83, 70, 80, 100, 93, 60]
management = [86, 73, 93, 83, 96, 63]
analysis = [80, 70, 100, 60, 93, 60]

arr = [[0] * 2 for i in range(6)]


for i in range(len(student)):
    arr[i][1] = i+1
    arr[i][0] = python[i] + management[i] + analysis[i]

for i in range(len(student)):
    print(arr[i][1], end = ' ')
print()
for i in range(len(student)):
    print(arr[i][0], end = ' ')
print()
for i in range(len(student)):
    print(arr[i][0]/3, end = ' ')
print()
arr.sort(reverse=True)

for i in range(len(student)):
    print(i+1,'등 -  총점: ',arr[i])
