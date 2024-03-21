def solution(dots):
    answer = 0

    for i in range(1,len(dots)):
        if(dots[0][0] == dots[i][0]):
            b =dots[i][1]
        if(dots[0][1] == dots[i][1]):
            c = dots[i][0]        
    d = dots[0][1]-b
    e = dots[0][0]-c
        
    answer = abs(d*e)
    return answer