import sys


def input_data():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    sensors = list(map(int, sys.stdin.readline().split()))

    return [N, K, sensors]


def solution():
    N, K, sensors = input_data()

    sensors = sorted(sensors)
    distances = []

    for i in range(1, len(sensors)):
        distance = sensors[i] - sensors[i - 1]
        distances.append(distance)

    distances = sorted(distances)
    print(sum(distances[:N - K]))


solution()
