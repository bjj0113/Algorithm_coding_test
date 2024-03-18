def solution(n):
    answer = 0
    for i in range(4,n+1):
        for k in range(2,i):
            if(i%k == 0):
                answer += 1
                break
    return answer