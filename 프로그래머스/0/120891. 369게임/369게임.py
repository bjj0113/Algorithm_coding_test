def solution(order):
    answer = 0
    for i in str(order):
        if(i == str(3) or i == str(6) or i==str(9)):
            answer += 1
    return answer