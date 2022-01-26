def makeMatrix (n, arr) :

    ret = []
    binarr = []
    [binarr.append(bin(e)[2:]) for e in arr]

    for element in binarr :

        while len(element) < n :
            element = '0' + element
        temp = []
        for e in element :
            temp.append(e)
        ret.append(temp)

    return ret


def solution(n, arr1, arr2):
    answer = []
    map1 = makeMatrix(n, arr1)
    map2 = makeMatrix(n, arr2)

    for i in range(n) :
        temp = []
        for j in range(n) :
            if map1[i][j] == '1' or map2[i][j] == '1' :
                temp.append('#')
            else :
                temp.append(' ')
        answer.append("".join(temp))

    return answer

if __name__ == '__main__' :
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))