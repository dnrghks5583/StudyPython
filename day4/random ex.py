# random 함수
#import random
from random import *

# print(random.choice(range(1, 7)))   # dice

# lottery
numbers = list(range(1, 46))
lottery = []

for i in range(6) :
    lottery.append(choice(numbers))
print(lottery)