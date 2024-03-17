def solution(n):
    cnt =0
    
    for x in range(1,n+1):
        if n%x == 0:
            cnt += 1
        
    return cnt