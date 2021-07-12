import sys

case = int(input())
index = 0
for i in range(case):
    index = 0
    sounds = list(map(str, sys.stdin.readline().strip().split()))
    while index == 0:
        animal = list(map(str, sys.stdin.readline().strip().split()))
        if animal[0] == "what":
            index = 1
            break

        for j in range(len(sounds)):
            if sounds[j] == animal[2]:
                sounds[j] = ""

    for i in range(len(sounds)):
        if sounds[i] != "":
            print(sounds[i], end=" ")




