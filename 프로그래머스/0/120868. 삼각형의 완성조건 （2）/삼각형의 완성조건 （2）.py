def solution(sides):
    answer = 0
    a = max(sides)
    b = min(sides)
    for i in range(a+b):
        if(a-b< i and i<a+b):
            answer += 1
        
    return answer