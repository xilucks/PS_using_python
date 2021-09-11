a = int(input())
list = []

for i in range(a):
    a,b = input().split()
    a,b = int(a), int(b)
    list.append([a,b])

def sort(list):
    return list[0], list[1]

ans = sorted(list, key=sort)

for i in range(len(ans)):
    print(" ".join(map(str,ans[i])))
