import sys


def input_data():
    actions = []

    for _ in range(10):
        actions.append(list(map(int, sys.stdin.readline().split())))

    return actions


def solution():
    actions = input_data()

    cards = list(i for i in range(1, 21))

    for action in actions:
        start_index, end_index = action[0], action[1]
        reversed_card = list(reversed(cards[start_index - 1: end_index]))
        cards = cards[:start_index - 1] + reversed_card + cards[end_index:]

    return cards


print(" ".join(list(map(str, solution()))))