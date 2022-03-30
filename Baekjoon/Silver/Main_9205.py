# 테스트 개수
from collections import deque

t = int(input())

# 테스트 개수 만큼 반복
for _ in range(t):

    state = 'sad'

    # 값 입력
    store_num = int(input())
    stores = []
    visit = [0] * store_num

    home = list(map(int, input().split()))
    for _ in range(store_num):
        stores.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))

    # 자료구조 세팅
    queue = deque()

    queue.append(home)
    # 연산
    while queue:
        x, y = queue.popleft()
        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
            state = 'happy'
            break

        for i in range(len(stores)):
            if visit[i] == 0:
                tmpx = stores[i][0]
                tmpy = stores[i][1]

                if abs(tmpx - x) + abs(tmpy - y) <= 1000:
                    visit[i] = 1
                    queue.append([tmpx, tmpy])

    print(state)


