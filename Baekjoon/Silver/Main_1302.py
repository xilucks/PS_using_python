import collections

books = collections.defaultdict(int)
N = int(input())

for _ in range(N):
    books[input()] += 1

max_num = 0
ans = ''
for book in books.keys():
    if books[book] > max_num:
        max_num = books[book]
        ans = book
    elif books[book] == max_num and ans > book:
        max_num = books[book]
        ans = book


print(ans)