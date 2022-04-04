N = int(input())

times = []

for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: x[0])
times.sort(key=lambda x: x[1])

ans = 0
now = 0

for i in range(len(times)):
    if now <= times[i][0]:
        ans += 1
        now = times[i][1]

print(ans)