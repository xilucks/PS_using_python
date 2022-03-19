import sys

str = input()


def solve(self, s: str) -> bool:
    arr = []
    for char in s:
        if s == ' ':
            continue
        arr.append(char.lower())

    while len(str) > 1:
        if str.pop(0) != str.pop():
            return False

    return True
