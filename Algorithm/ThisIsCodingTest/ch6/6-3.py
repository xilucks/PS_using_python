# 180p 성적이 낮은 순서로 학생 출력하기

N = int(input())

arr = []
for _ in range(N):
    inf = list(input().split())
    name = inf[0]
    score = int(inf[1])
    arr.append((name, score))


def setting(data):
    return data[1]


arr.sort(key=setting)

for i in range(len(arr)):
    print(arr[i][0])
