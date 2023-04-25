import sys

my_team_score = list(map(int, sys.stdin.readline().split()))
other_team_score = list(map(int, sys.stdin.readline().split()))

my_team_total = 0
other_team_total = 0

a_win_count = 0
b_win_count = 0

for index in range(len(my_team_score)):
    my_team_total += my_team_score[index]
    if my_team_total > other_team_total:
        a_win_count += 1

    other_team_total += other_team_score[index]
    if my_team_total < other_team_total:
        b_win_count += 1


if other_team_total > my_team_total and a_win_count >= 1:
    print('Yes')
else:
    print('No')

