#두 수의 합
#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

#input: nums = [2,7,11,15], target = 9
#output 0,1

import sys

#01 Brute-Force
num = list(map(int, sys.stdin.readline().strip().split()))
target = int(input())

for i in range(len(num)):
   for  j in range(i+1, len(num)):
       if num[i] + num[j] == target :
           print(i, j)
           break

print('----------------------')
#02 in을 이용한 탐색
# Target에서 n을 빼고, 그 값이 배열안에 존재하는지를 탐색
for i, n in enumerate(num):
    complement = target - n

    if complement in num[i+1:] :
        print(num.index(n), num[i+1:].index(complement)+(i+1))


#03 dictionary를 이용한 탐색 속도 개선

nums_map = {}

for i, n in enumerate(num):
    nums_map[n] = i

for i, n in enumerate(num):
    if target - n in nums_map and i != nums_map[target-n]:
        print(i, nums_map[target - n])


#04 조회 구조 개선

for i, n in enumerate(num):
    if target - n in nums_map:
        print(nums_map[target - n], i)
        break

    nums_map[n] = i


#05 투 포인터 이용

#정렬이 되어있지 않으므로 사용할 수 없다.
#딕셔너리로 index값 정렬하고 배열한다음 써보면?
