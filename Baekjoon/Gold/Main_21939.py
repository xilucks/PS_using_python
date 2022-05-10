import collections
import heapq

problem_num = int(input())

max_heap, min_heap = [], []
problems = collections.defaultdict(bool)

for _ in range(problem_num):
    problem_num, level = map(int, input().split())
    heapq.heappush(max_heap, [-level, -problem_num])
    heapq.heappush(min_heap, [level, problem_num])
    problems[problem_num] = True

command_num = int(input())

for _ in range(command_num):
    commands = list(map(str, input().split()))
    num = int(commands[1])

    if commands[0] == "recommend":
        if num == 1:
            while not problems[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])

        else:
            while not problems[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])

    elif commands[0] == "add":
        while not problems[-max_heap[0][1]]:
            heapq.heappop(max_heap)

        while not problems[min_heap[0][1]]:
            heapq.heappop(min_heap)

        level = int(commands[2])
        heapq.heappush(max_heap, [-level, -num])
        heapq.heappush(min_heap, [level, num])
        problems[num] = True

    else: #solved
        problems[num] = False
