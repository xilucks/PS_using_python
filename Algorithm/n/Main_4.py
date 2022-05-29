players = [0, 99, 1, 1, 1, 23, 1, 1]
power= 0
k = 0

def solution(players, power, k):
    dp = [[0] * 2 for _ in range(len(players)+1)]
    dp[0][0], dp[0][1] = power, power
    combo = 1
    for i in range(len(players)):
        player_power = players[i]
        index = i+1

        if player_power > dp[i][0]:
            dp[index][0], dp[index][1] = max(dp[i][0], dp[i][1]) + k, max(dp[i][0], dp[i][1]) + k
            combo = 1

        else:
            dp[index][1] = max(dp[i][0], dp[i][1]) + k

            dp[index][0] = dp[i][0] + combo
            combo += 1
    print(dp)

    ans = max(dp[len(players)][0], dp[len(players)][1])

    return ans




print(solution(players, power, k))