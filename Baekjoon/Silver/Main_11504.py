import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    count = 0
    N, M = map(int, sys.stdin.readline().strip().split())

    X = list(map(str, sys.stdin.readline().split()))
    minimum = int("".join(X))

    Y = list(map(str, sys.stdin.readline().split()))
    maximum = int("".join(Y))

    board = list(map(str, sys.stdin.readline().strip().split()))
    for i in range(len(board)):
        test_num = "".join(board[i: i + M])

        if len(str(test_num)) < M:
            require_count = M - len(str(test_num))
            test_num = str(test_num) + "".join(board[:require_count])

        count = count + 1 if (minimum <= int(test_num) <= maximum) else count
    print(count)

