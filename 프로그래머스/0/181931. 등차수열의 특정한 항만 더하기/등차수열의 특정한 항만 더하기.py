def solution(a, d, included):
    answer = 0
    # a + d*n n은 0부터
    for i,k in enumerate(included):
        if k == True:
            answer = answer + (a + (d * i))
    return answer