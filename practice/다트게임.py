def solution(dartResult) :
    stack = []
    flag = False

    for result in dartResult :

        dic = {'S' : 1, 'D' : 2, 'T' : 3}
        if result == '1' :
            flag = True
        
        elif result == '0' and flag :
            stack.pop()
            stack.append(10)
            flag = False
            continue

        if result >= '0' and result <= '9' :
            stack.append(int(result))
         
        elif result == '*' :
            
            flag = False
            if len(stack) == 1 :
                stack[0] = stack[0] * 2
                continue
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * 2)
            stack.append(n1 * 2)
        
        elif result == '#' :
            flag = False
            n = stack.pop()
            stack.append(-n)
        
        else :
            flag = False
            n = stack.pop()
            stack.append(n ** dic[result])

    return sum(stack)

if __name__ == '__main__' :
    dartResult = '1D2S#10S'
    print(solution(dartResult))