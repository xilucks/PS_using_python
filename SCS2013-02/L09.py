#E-1
lst_1=[]
for num in range(1,11):
  lst_1.append(num**3)

print(lst_1)

#E-2
coin = ['h','t']

lst_2 = []
for i in coin :
  for j in coin:
    lst_2.append(i+j)
print(lst_2)

#E-3
vowels = ['a','e','i','o','u']

def pick_voewls(str):
  lst = []
  for i in str:
    if i in vowels:
      lst.append(i)

  return lst

#E-4
print([a+b for a in [10,20,30] for b in [1,2,3]])
n_list = []
# your code here: using two for loops
for a in [10,20,30]:
  for b in [1,2,3]:
    n_list.append(a+b)

print(n_list)

#E-5
q_list = [[x,y] for x in range(-5,6) for y in range(0,11) if y == x**2+1]

#E-6
def unique_list(n_list):
  u_list = []
  for i in n_list:
    if not i in u_list:
      u_list.append(i)
  return u_list


#input E-1
word1,word2,word3 = input().split()
print(f"{word1}**{word2}**{word3}")

#input E-2
def report_GPA():
  # take user input to ask number of classes taken and assign it to variable `num_classes`

  num_classes = int(input())

  # class and grade list
  class_list = []
  grade_list = []

  # Using a for loop, take user inputs of name of each class and corresponding grade,
  for i in range(num_classes):
    print(f"class {i+1}")
    class_name = input()
    class_grade = input()

    class_list.append(class_name)
    grade_list.append(class_grade)
  # and add it to class_list and grade_list
    overall_gpa = sum(grade_list)/len(grade_list)
  print('Class list:', class_list)
  print('Grade list:', grade_list)

  # compute the overall gpa as an average of grades

  print(f'Overall GPA: {overall_gpa}')


#input E-3

def upper_lower():
  num_upper = 0
  num_lower = 0;

  my_str = input()

  for i in my_str:
    if i.isupper():
      num_upper += 1
    elif i.islower():
      num_lower += 1
    else:
      continue

  print(num_upper, num_lower)

upper_lower()