def solution(num_list):
    answer = 0
    for x in num_list:
        y = x
        while y>1:
            if y%2 == 0:
                y= y/2
                answer += 1
            else:
                y = (y-1)/2
                answer += 1
    return answer