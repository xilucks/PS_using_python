#E-1
def write_file(fname, str_list):
    with open(fname, mode = 'w') as f:
        for my_str in str_list:
            f.write(my_str+"\n")
    print(f.read())
#E-2
def read_last_file(fname, n):
    with open(fname, mode = "r") as f:
        line = f.readline()[-n:]

    return line

#E-3
def count_line_files(fname):
    with open(fname, mode ='r') as f:
        lines = f.readline()
    return len(lines)
#E-4
def count_words_file(fname):
    with open(fname, mode = 'r') as f:
        return len(f.read().split())
#E-5
def read_odd_file(fname):
    with open(fname, mode = 'r') as f:
        lines = []

        for index, line in enumerate():
            if index % 2 == 0:
                lines.append(line)

    return lines

#E-6
def count_words(fname, my_word):
    with open(fname, mode = 'r') as f:
        count = 0
        words = f.read().split()

        for word in words :
            if word == my_word:
                count += 1

    return count

#E-7

try:
    import pricing
    print('OK: ')
except:
    print('Fail')