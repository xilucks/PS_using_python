# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며,
# 구두점(마침표, 쉼표 등) 또한 무시한다.
import collections
import re

paragraph = input()
banned = []
a = input()
banned.append(a)

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if not word in banned]

counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1

print(max(counts, key=counts.get))