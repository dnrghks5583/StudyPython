def jaccard(str1, str2) :
    
    if len(str1) == 0 and len(str2) == 0 :
        return 1
    dic1 = makeDict(str1)
    dic2 = makeDict(str2)
    unionDic = makeDict(str1 + str2)
    return intersection(dic1, dic2, unionDic) / union(dic1, dic2, unionDic)

def makeDict(arr) :
    
    dic = {}
    for e in arr :
        dic[e] = arr.count(e)
    return dic

def intersection(dic1, dic2, unionDic) :

    ret = 0
    for e in unionDic.keys() :
        if e not in dic1 or e not in dic2 :
            continue
        ret += min(dic1[e], dic2[e])
    return ret

def union(dic1, dic2, unionDic) :
    
    ret = 0
    for e in unionDic.keys() :
        if e in dic1 and e in dic2 :
            ret += max(dic1[e], dic2[e])
        elif e in dic1 :
            ret += dic1[e]
        elif e in dic2 :
            ret += dic2[e]
    return ret

def check(c) :
    if c <= 'Z' and c >= 'A' :
        return True
    return False

def ngram(string) :

    arr = []
    string = string.upper()
    idx = 0
    while idx + 2 <= len(string) :
        if check(string[idx]) and check(string[idx+1]) :
            arr.append(string[idx : idx + 2])
        idx += 1
    return arr

def solution(str1, str2) :
    
    strList1 = ngram(str1)
    strList2 = ngram(str2)

    return int(jaccard(strList1, strList2) * 65536)

if __name__ == '__main__' :
    str1 = 'aa1+aa2'
    str2 = 'AAAA12'
    print(solution(str1, str2))