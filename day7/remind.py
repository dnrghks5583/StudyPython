import numpy as np

print('One dimension')

a = [1, 2, 3, 4]

print(type(a))
print(len(a))

print('Two dimension')

a = [[2, 3], [3, 3, 4]]

print(len(a))

# a = a + 2 error
a = [[1, 2, 3, 4], [3, 5, 7, 9]]
a = np.array(a)
print(a * 2)
print(np.shape(a))