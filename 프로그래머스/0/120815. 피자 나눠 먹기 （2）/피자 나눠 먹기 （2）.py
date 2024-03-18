#6과 n의 최소공배수 구해서 6으로 나누기
def solution(n):
    answer = 0
    
    for x in range(max(6,n),6*n+1):
        if(x%6==0 and x%n == 0):
            answer = x/6
            break
    
    return answer