import collections
import sys

case = int(sys.stdin.readline())

for _ in range(case):
    card_num = int(sys.stdin.readline())
    before_cards = list(map(str, sys.stdin.readline().strip().split()))
    after_cards = list(map(str, sys.stdin.readline().strip().split()))

    before_card_dict = collections.defaultdict(int)
    after_cards_dict = collections.defaultdict(int)

    isTrue = True

    for index in range(len(before_cards)):
        before_card_dict[before_cards[index]] += 1
        after_cards_dict[after_cards[index]] += 1

    for key in before_card_dict.keys():
        if before_card_dict[key] != after_cards_dict[key]:
            isTrue = False
            break

    print("NOT CHEATER" if isTrue else "CHEATER")


