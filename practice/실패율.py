# 전체 스테이지 수 N

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages) :

    arr = []
    failure = []
    [arr.append (stages.count(i)) for i in range(1, N + 2)]

    for stage in range(1, N + 1) :

        if arr[stage - 1] == 0 :
            failure.append((0, stage))
            continue
        failure.append((arr[stage - 1]/sum(arr[stage - 1 : N + 1]), stage))
    
    failure.sort(reverse = True, key = lambda x : (x[0], -x[1]))
    ret = []
    [ret.append(s[1]) for s in failure]
    return ret

if __name__ == '__main__' :
    print(solution(N, stages))