# Data Type
print(None)
print(type(None))

print(None == 0)
a = None
print(a)
print(type(a))

# 숫자형
금액 = 12_345_678
print(금액)

# 문자열
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)

bruce_eckel = 'Life is short, \nYou need Python'
print(bruce_eckel)

# print('\\') -> \
# 여러줄 bruce = '''
#
# '''

# boolean
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
# print(val_sum = 100) x
bl_true = True
print(bl_true)
print(type(bl_true))
print(bl_true == True)  # true
print(bl_true is True)  # true

print(a is None)        # true
print(val_sum is 1000)  # true

# 의미가 있는 bool
print(bool(1))          # true 
print(bool(0))          # false

# list
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i for i in range(54)]
print(b)

arr2 =  ['Life', 'is', 'short',
         'U', 'need', 'Python', 3]
print(arr2)

arr3 = [[1, 2, 3], [4, 5 ,6]]
print(arr3)

# empty list
arr4 = list()
print(arr4)

# tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# dictionary
spiderman = {'name' : '피터 파커', 
             'age' : 18, 
             'weapon' : '웹슈터'}
print(spiderman)

# 집합
set_int = set([1, 2, 3, 4, 5, 4, 6, 7, 1, 2, 2])
print(set_int)
