
c = chr(ord('a')-32)
print(c)

print(round(3.14,1))
a = 3.123124
print("{:.1f}".format(a))

numbers = [0,1,2,3,4,5]
print(numbers[:3])
del numbers[3]
numbers.append(4)
numbers.insert(2,12)
print(numbers)
new_list = sorted(numbers, reverse=True)
print(new_list)
numbers.sort(reverse = True)
print(numbers)

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)