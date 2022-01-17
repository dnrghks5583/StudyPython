# 리스트 연산
arr = list(range(5))
print(arr)

arr = list(range(1, 6))
print(arr)

arr = list(range(2, 101, 2))
print(arr)
print(arr[0] + arr[5])

# 2차원 배열(list)
arr2 = [1, 2, ['Hi', 'My', 'Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0])

arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 3)
# print(arr3 + 3)    불가능
print(arr3 + arr)    # 가능
print(len(arr))

# list function
print('----- List function -----')
# 원소 삭제
del(arr3[1])    # index로 삭제
print(arr3)

arr3.remove(1)  # value로 삭제
print(arr3)

arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)
print(arr4)
del(arr4[8])
print(arr4)

arr4.sort()
print(arr4)

arr4.reverse()
print(arr4)

arr4.insert(2, 10)
print(arr4)

arr4[0] = 108
print(arr4)

tup1 = tuple(range(1, 6))
print(tup1)
print(tup1[3])

# dictionary
dict1 = {1 : 'a'}
dict1[2] = 'b'
print(dict1)

dict1['name'] = 'Hugo'
print(dict1)

del dict1['name']
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

# list to tuple
tup2 = tuple(arr4)
print(tup2)

# tuple to list
arr5 = list(tup1)
print(arr5)
arr5.append(6)
print(arr5)
tup1 = tuple(arr5)
print(tup1)