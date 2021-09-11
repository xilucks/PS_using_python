N = int(input())
list = []
for i in range(N):
    a = input()
    list.append(a)

def al(list):
    return len(list), list

ans = set(list)
ans = sorted(ans, key=al)


print("\n".join(ans))