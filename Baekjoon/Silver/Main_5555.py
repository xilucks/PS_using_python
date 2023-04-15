import sys


def input_data():
    target = sys.stdin.readline().strip()
    rings_num = int(sys.stdin.readline().strip())
    rings = []

    for _ in range(rings_num):
        rings.append(sys.stdin.readline().strip())

    return [target, rings]


def solution():
    [target, rings] = input_data()
    ans = 0

    for ring in rings:
        for index in range(len(ring)):
            string = ''
            for length in range(len(target)):
                string += ring[(index + length) % len(ring)]
            if string == target:
                ans += 1
                break

    print(ans)


solution()
