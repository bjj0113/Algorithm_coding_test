def solution(s):
    answer = True
    x = []
    for k in s:
        if k == '(':
            x.append(1)
        else:
            if len(x) == 0:
                answer = False
                break
            x.pop()
    
    if len(x) != 0:
        answer = False
    return answer