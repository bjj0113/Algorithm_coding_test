def solution(a, b):
    answer = 0
    
    d = 2 * a * b
    
    c = str(a) +  str(b)

    
    if(d > int(c)):
        answer = d
    else:
        answer = int(c)
    return answer