import re
print("1/////////////////////////")
#E-1
target_str = 'Emma is a baseball player who was born on June 17'

# sol: search()
pattern = r'\b\w{8}\b'
result = re.search(pattern, target_str)

# print the match object:
if result:
  print(f'Match object: {result}')
  print(f'Matching word: {result.group()}')
  print("2/////////////////////////")
#E-2
target_str = 'EMMA is a baseball player who was born on June 17 and takes a class Python Programming'

# sol: findall()
pattern = r'[A-Z]\w*'
result = re.findall(pattern,target_str)

print(result)
print("3/////////////////////////")
#E-3
target_str = 'Emma is a baseball player who was born on June 17 and she loves to play with a ball'

# sol: findall()
pattern = r'\bball\b|\bplayer\b'
result = re.findall(pattern,target_str)

print(result)
print("4/////////////////////////")
#E-4
target_str = 'James is a Python developer. He took a class of Python Programming'

# sol: findall()
pattern = r'\b[P]\w*[g]\b'
result = re.findall(pattern,target_str)

print(result)
print("5/////////////////////////")
#E-5
target_str = 'Kelly loves banana and apple'

# sol: findall()
pattern = r'\b[a]\w*\b|\b\w*[a]\b'
result = re.findall(pattern,target_str)

print(result)
print("6/////////////////////////")
#E-6
target_str = 'Korea: co.kr, USA: com, UK: co.uk'

# sol: split()
pattern = r'[:,\s]\s*'
result = re.split(pattern,target_str)

print(result)
print("/////////////////////////")
#E-7
target_str = '   James knows Python    and   machine  learning  \n'

# sol: sub()
pattern = r'\s+'
new_pattern = ' '
new_str = re.sub(pattern,new_pattern,target_str)

print(target_str)
print(new_str)