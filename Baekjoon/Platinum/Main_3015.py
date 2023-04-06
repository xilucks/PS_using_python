import sys


def input_data():
    N = int(sys.stdin.readline())
    nums = []

    for _ in range(N):
        nums.append(int(sys.stdin.readline()))

    return nums


def solution():
    nums = input_data()
    stack = []
    ans = 0

    for num in nums:
        while stack and stack[-1][0] < num:
            data = stack.pop()
            ans += data[1]

        if len(stack) == 0:
            data = [num, 1]
            stack.append(data)

        # 같을 때
        elif stack[-1][0] == num:
            ans += stack[-1][1]
            data = stack.pop()
            if stack:
                ans += 1
            stack.append([data[0], data[1] + 1])

        # 스택에 들어가 있는 수가 방금 만난 수보다 클 때
        else:
            data = [num, 1]
            stack.append(data)
            ans += 1

    print(ans)


solution()