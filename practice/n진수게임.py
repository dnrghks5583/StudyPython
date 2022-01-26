def convert(n, number) :

    dic = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    arr = []
    if number == 0 :
        return '0'

    while number > 0 :
        
        r = number % n
        number //= n
        if r >= 10 :
            arr.append(dic[r])
            continue
        arr.append(str(r))

    return "".join(arr[::-1])

def solution(n, t, m, p):
    
    answer = ''
    temp = ''
    for i in range(p + t * m + 1) :
        temp += convert(n, i)
    answer = temp[p - 1: : m]
    return answer[:t]

if __name__ == '__main__' :
    n = 16
    t = 16
    m = 2
    p = 1
    print(solution(n, t, m, p))