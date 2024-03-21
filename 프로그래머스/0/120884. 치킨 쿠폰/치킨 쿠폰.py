def solution(chicken):
    answer = -1
    svc = chicken//10
    rem = chicken%10+svc
    if(rem>=10):
        svc += solution(rem)
    
    return svc