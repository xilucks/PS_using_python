#E-1
import random


num_list = [random.randrange(100,1000) for i in range(100)]
print(num_list)
two_nums = random.sample(num_list, k=2)

#E-2
my_str = "hihihi Hihihihi"
one_char = random.choice(my_str)

#E-3
dice = [1,2,3,4,5,6]
for i in range(10):
    print(f'{random.choice(dice)}')
    print(f'{random.randint(1,6)}')

#E-4
from datetime import datetime

my_date = datetime(2021,12,2).date()
my_year = my_date.year
my_month = my_date.month
my_day = my_date.day

#E-5
import numpy as np

my_arr = np.arange(10, 100, 10).reshape(3,3)
print(my_arr)
#E-6

my_arr = np.arange(3,61,3).reshape(5,4)
new_arr = my_arr[::2, 1::2]
print(new_arr)

#E-7

my_arr = np.random.randint(10,100,(3,4))
mean_now = my_arr.min(axis=0)
std_now = my_arr.std(axis=0)

mean_column = my_arr.mean(axis=1)
std_column = my_arr.std(axis=1)


#E-8
num_max = my_arr.max()
num_min = my_arr.min()

new_arr = (my_arr - num_min)/(num_max - num_min)