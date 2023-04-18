import sys


def input_data():
    test_case = int(sys.stdin.readline())

    case = []

    for _ in range(test_case):
        record_num = int(sys.stdin.readline())

        left_record = list(map(int, sys.stdin.readline().split()))
        right_record = list(map(int, sys.stdin.readline().split()))

        case.append([record_num, left_record, right_record])

    return case


def solution():
    case_list = input_data()

    for case in case_list:
        left_come = 0
        [record_num, left_record, right_record] = case

        left_start_times = []
        for left_time in left_record:
            if len(left_start_times) == 0 or not left_time - 500 in left_start_times:
                left_start_times.append(left_time)

        for right_time in right_record:
            if right_time - 1000 in left_start_times:
                left_come += 1

        print(left_come)


solution()