
def solution(my_string):
    answer = 0
    for x in my_string:
        if(x.isdigit()):
            answer += int(x)
    return answer