def solution(A, B):
    answer = 0
    x = list(A)
    z = list(B)
    i = 0
    for _ in range(len(x)):
        if(x == z):
            answer = i
            break
        y = x.pop()
        x.insert(0,y)
        i+=1
        
    if(i ==len(x)):
        return -1
    return answer