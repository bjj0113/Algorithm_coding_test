def solution(age):
    alpha = "abcdefghijklmnopqrstuvxyz"
    x = list(alpha)
    y = list(str(age))
    z = []
    for i in range(len(y)):
        z.append(x[int(y[i])])
    
    answer = ''.join(z)
    return answer