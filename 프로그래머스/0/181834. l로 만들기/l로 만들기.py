def solution(myString):
    answer = ''
    for i,k in enumerate(myString):
        if k < 'l':
            k = 'l'
        answer += k
    return answer