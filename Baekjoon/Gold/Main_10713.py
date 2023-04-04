import collections
import sys


def input_data():
    N, M = map(int, sys.stdin.readline().split())
    road = list(map(int, sys.stdin.readline().split()))
    train = []

    for _ in range(N - 1):
        train.append(list(map(int, sys.stdin.readline().split())))

    return [[N, M], road, train]


def solution():
    [N, M], road, train = input_data()
    ans = 0

    visit_city_list = []

    for i in range(len(road) - 1):
        start = road[i]
        end = road[i + 1]
        start_range = start if start < end else start
        end_range = end if start < end else end
        move = 1 if start < end else -1
        for city_name in range(start_range, end_range, move):
            visit_city_list.append(city_name)

    visit_city_list.append(road[len(road) - 1])

    train_dict = collections.defaultdict(int)

    for i in range(len(visit_city_list) - 1):
        now_city = visit_city_list[i]
        next_city = visit_city_list[i + 1]

        start = now_city if now_city < next_city else next_city
        train_dict[start] += 1

    train_names = list(train_dict.keys())

    for train_name in train_names:
        train_info = train[train_name - 1]
        train_num = train_dict[train_name]
        ticket_price, ic_price, ic_card_price = train_info

        ticket_case = ticket_price * train_num
        ic_case = ic_card_price + (ic_price * train_num)

        if ticket_case > ic_case:
            ans += ic_case
        else:
            ans += ticket_case

    print(ans)


solution()
