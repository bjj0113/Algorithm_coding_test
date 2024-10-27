def solution(ineq, eq, n, m):
    x =''
    if eq == '=':
        x = str(n) + ineq + eq + str(m)
    elif eq == '!':
        x = str(n) + ineq + str(m)

    if eval(x):
        answer = 1
    else:
        answer = 0
    
    return answer