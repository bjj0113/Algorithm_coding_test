def solution(l, r):
    answer = []
    for i in range(l,r+1):
        x = i
        y = str(x).replace('5','')
        y = y.replace('0','')
        if  y == '':
            answer.append(i)
    
    if not answer:
        answer.append(-1)
    return answer