from math import sqrt

def convert(n, k) :

    arr = []
    while n > 0 :
        
        r = n % k
        n //= k
        arr.append(str(r))

    return ''.join(arr[::-1])

def isPrime(n) :
    
    if n == 2 or n == 3 : return True
    if n == 1 or n % 2 == 0 : return False

    for i in range( 2, int( sqrt(n) ) + 1) :
        if n % i == 0 :
            return False
    return True

def solution(n, k):

    answer = 0
    ret = convert(n, k).split('0')
    for num in ret :
        if num == '' : continue
        if isPrime(int(num)) :
            answer += 1
    return answer

if __name__ == '__main__' :
    n = 110011
    k = 10
    print(solution(n, k))