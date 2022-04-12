#

str = input()
major, name = str.split(':')

print('********')

print('나는 동국대학교 {0} 학과 {1}입니다.'.format(major, name))

major, tmp, name = str.partition(':')

print('나는 동국대학교 {0} 학과 {1}입니다.'.format(major, name))

segment_index = str.index(':')

print('나는 동국대학교 {0} 학과 {1}입니다.'.format(str[:segment_index], str[segment_index+1:]))

