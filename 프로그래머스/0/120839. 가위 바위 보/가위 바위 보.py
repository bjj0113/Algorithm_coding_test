def solution(rsp):
    answer = ''
    for x in rsp:
        if(x == '0'):
            answer += str(5)
        elif(x == '2'):
            answer += str(0)
        else:
            answer += str(2)
    return answer