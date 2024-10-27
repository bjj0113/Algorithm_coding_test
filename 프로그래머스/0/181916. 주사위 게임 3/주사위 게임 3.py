def solution(a, b, c, d):
    answer = 0
    z = [a,b,c,d]
    x = set([a,b,c,d])
    y = []
    if len(x) == 4:  #모두 다른 경우
        answer = min(a,b,c,d)
        
    elif len(x) == 3: #두개만 같은 경우 2/1/1
        for i in x:
            if z.count(i) == 1:
                y.append(i)
        answer = y[0] * y[1]
            
    elif len(x) == 2: # 3/1 2/2
        p, q = 0, 0
        for i in x:
            if z.count(i) == 1:
                q = i
            elif z.count(i) == 3:
                p = i
            else:
                y.append(i)  
        if q: # 3/1
            answer = (10 * p + q)**2
        else: # 2/2
            answer = (y[0] + y[1]) * abs(y[0] - y[1])
    else: # 모두 같은 경우 len(x) == 1
        answer = 1111 * a
    
    return answer