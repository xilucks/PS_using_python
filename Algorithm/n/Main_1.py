card1 = [[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]
card2 = [[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]


def solution(cards1, cards2):
    game = len(cards1)
    answer = 0

    for i in range(game):
        player_one, player_two = cards1[i], cards2[i]
        cards = player_one + player_two
        cards_set = set(cards)

        if len(cards) != len(cards_set):
            answer += 1

        else:
            if i == 0:
                continue

            else:
                count1, count2 = 0, 0
                for c1 in cards1[i]:
                    if c1 in cards1[i-1]:
                        count1 += 1
                for c2 in cards2[i]:
                    if c2 in cards2[i-1]:
                        count2 += 1

                if count1 >= 2 or count2 >= 2:
                    answer += 1

    return answer

print(solution(card1, card2))

