def solution(strArr):
    answer = 0
    x = []
    y = []
    for k in strArr:
        x.append(len(k))

    for i in set(x):
        y.append(x.count(i))
    
    answer = max(y)
            
    return answer