# exception handling

def add(a, b) :
    return a + b

def minus(a, b) :
    return a - b 

def multiple(a, b) :
    return a * b

def divide(a, b) :
    return a / b

print('사칙연산 시작')

a, b = 4, 1
numbers = [3, 6, 9]

try :
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[1]) * 4
    num = int(input('수를 입력하세요 : '))

except ZeroDivisionError as e :
    print(f'나누기 예외 발생! 추가처리1 {e}')

except IndexError as e :
    print(f'예외 발생! 추가처리2 {e}')

except ValueError as e :
    print(f'숫자만 넣으세요  {e}')

except Exception as e :
    print(f'예외 발생! 추가처리3 {e}')

finally : # 예외가 발생하든 안하든 무조건 실행
    print(f'곱하기 결과 : {multiple(a, b)}')
    print(f'  빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')

print('사칙연산 종료')