import collections
import sys
from typing import Deque

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

def solve_2(self, s: str) -> bool :
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum:
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False