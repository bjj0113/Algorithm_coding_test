def solution(a, b):
    answer = 0
    if(a%2==0 and b%2 ==0): # 둘다 짝수
        answer = abs(a-b)
    elif(a%2==1 and b%2==1): #둘다 홀수
        answer = a*a+b*b
    else:
        answer = 2*(a+b)
    return answer