import sys


def input_data():
    N = int(sys.stdin.readline())
    cranes = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    boxes = list(map(int, sys.stdin.readline().split()))

    return [N, cranes, M, boxes]


def solution():
    [N, cranes, M, boxes] = input_data()
    sort_cranes = sorted(cranes, reverse=True)
    sort_boxes = sorted(boxes, reverse=True)

    time = 0

    if sort_boxes[0] > sort_cranes[0]:
        return -1

    while sort_boxes:
        for crane in sort_cranes:
            for box in sort_boxes:
                if crane >= box and boxes:
                    sort_boxes.remove(box)
                    break

        time += 1

    return time


print(solution())
