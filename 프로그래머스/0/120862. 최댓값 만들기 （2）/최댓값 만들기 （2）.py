def solution(numbers):
    answer = 0
    numbers.sort()
    a= numbers[-1]
    c= numbers[-2]
    b= numbers[0]
    d= numbers[1]
    if(a*c>b*d):
        answer = a*c
    else:
        answer = b*d
    return answer