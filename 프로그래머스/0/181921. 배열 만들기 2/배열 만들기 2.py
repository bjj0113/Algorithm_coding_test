def solution(l, r):
    answer = []
    for i in range(l,r+1):
        x = i
        y = set(list(str(x))) - set('05')
        
        if not y:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer