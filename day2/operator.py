# 연산자 (사칙연산)
a = 11
b = 4

print(a +  b)
print(a -  b)
print(a *  b)
print(a /  b)
print(a // b)
print(a %  b)

# 문자열 연산
stat1 = 'hello'
stat2 = 'world'
res = stat1 + stat2
print(res)
print(stat1 + stat2)
print(stat1,  stat2)
res = stat1, stat2
print(res)
# 문자열 연산에서는 *, + 만 있음
# print(stat1 - stat2) 문자열 빼기 없음
print(stat1 * 5)
# print(stat1/3) 문자열 나누기 없음 
# print(stat1 * stat2) 문자열끼리 곱하기 없음 

# 문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일
print(stat3[0])
print(stat3[1])
print(stat3[2])
print(stat3[3])
print(stat3[4])
print('--------------')
# print(stat3[5]) out of range

# 문자열 값 변경 x
# stat3[0] = '저'
# stat3[1] = '리'
# print(stat3)

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

# 문자열 자르기
일시 = '2022-01-17 14:39:25'
print(일시[:4], '년')
print(일시[5:7], '월')
print(일시[8:10], '일')
print(일시[11:13], '시')
print(일시[14:16], '분')
print(일시[-2:], '초')

print(일시[-5:-3], '분')

# list
list_a = [1, 2, 3, 4, 5]
list_a[1] = 19
print(list_a)

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

# 문자열 fomat
첫번째 = '투'
두번째 = '유'
str1 = "I'm so happy {0} U. are {1} ?".format(첫번째, 두번째)
print(str1)

str2 = f"I'm so happy {첫번째} U. are {두번째} ?"
print(str2)

# 숫자 천단위
money = 1000000000
print(format(money, ',d'))

# import datetime as dt
# now = dt.datetime.now()
# print(now)
# print(now.strftime('%Y년 %m월 %d일 %H:%S:%S'))

import math

myPI = math.pi
print(myPI)

print('{0}'.format(myPI))
print('{0:0.2f}'.format(myPI))
print(f'{myPI:0.6f}')

full_name = 'K U H'
age = 26
print(f'''안녕하세요. 저는 {full_name}입니다. 
나이는 {age}살 이구요.''')

part_name = full_name.split()
print(part_name)

test = 'Hey, guys'
print(test.split(','))
code = 'TEST|20222|01|17|F45678'
split_code = code.split('|')
print(split_code)

# 단어 교체
print(full_name.replace('K', 'Ashleuy'))

# 공백 제거
aaa = '    Hello, World!      '
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())

# index()
print(full_name.index('U'))
# print(full_name.index('a')) 못 찾으면 에러

# find()
print(full_name.find('X')) # Output : -1, X not in full_name

# count()
print(full_name.count('U'))

print('-'.join(full_name))

print(full_name.upper())
print(full_name.lower())
