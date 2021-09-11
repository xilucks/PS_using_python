#그룹 애너그램
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
#애너그램 : 문자를 재 배열하여 다른 뜻을 가진 단어로 바구는 것.
# ex) ate eat tea
import collections
import sys

List = list(map(str, sys.stdin.readline().strip().split()))

anagrams = collections.defaultdict(list);

for word in List :
    anagrams[''.join(sorted(word))].append(word)

print(list(anagrams.values()))

