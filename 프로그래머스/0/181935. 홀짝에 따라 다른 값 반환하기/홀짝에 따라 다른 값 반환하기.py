def solution(n):
    answer = 0
    
    if n%2 ==1:
        for a in range(n+1):
            if a%2 == 1:
                answer += a
    else:
        for a in range(n+1):
            if a%2 == 0:
                answer += a**2
    
    return answer