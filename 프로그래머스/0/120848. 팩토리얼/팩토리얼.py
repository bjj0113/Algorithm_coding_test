def solution(n):
    answer = 0
    fac = 1
    for x in range(1,11):
        fac *= x
        if(fac<=n):
            answer = x
    return answer