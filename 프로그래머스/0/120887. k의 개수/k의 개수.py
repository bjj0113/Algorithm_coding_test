def solution(i, j, k):
    answer = 0
    for x in range(i,j+1):
        a = list(str(x))
        for y in a:
            if(y == str(k)):
                answer += 1
    return answer