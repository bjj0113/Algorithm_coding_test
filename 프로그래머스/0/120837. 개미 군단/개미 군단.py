def solution(hp):
    answer = 0
    
    a = 5
    b = 3
    c = 1
    
    answer += hp//a
    answer += (hp%a)//b
    answer += (hp%a)%b//c

    return answer