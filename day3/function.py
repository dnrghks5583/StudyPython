# 함수 선언 및 사용

# add operator function definition
def add(a, b) :
    return a + b

print(add(2464, 879))

# function 종류
# 1. 매개변수가 없는 형태
def say_hello():
    print('hello')

def say_hello2():
    return 'hello~'

say_hello()
print(say_hello2())
print(say_hello2(), 'my friend')

val = say_hello2()
print(val.replace('o~', ' '))

# 2. 결과 값이 없는 형태
def say_hello(name) :
    print(f'Hello~ {name}')

say_hello('Hugo')

# 3. 매개변수, 결과 값 둘 다 없는 형태
def say_goodbye() :
    print('Bye bye~')

say_goodbye()

# 4. 매개변수 지정 
def  multi(a, b) :
    return a  * b

print(multi(2, 9))
print(multi(8, 9))

# 5. 매개변수 개수가 가변적인 경우
def plus(*args) :
    
    sum = 0
    for i in args :
        sum += i
    return sum

print(plus(1, 2, 3))
print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 6. 함수 결과가 하나 이상인 경우
def mult_and_div(x, y) :
    return x * y, x / y

res1, res2 = mult_and_div(7, 8)
print(res1, res2)

def oper(x, y) :
    return x + y, x - y,  x * y, x / y
res = oper(9, 5)
print(res)
print(type(res))