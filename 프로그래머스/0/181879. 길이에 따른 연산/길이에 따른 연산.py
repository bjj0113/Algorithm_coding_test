def solution(num_list):
    answer = 0
    i = len(num_list)
    mul=1
    if i>10:
        answer = sum(num_list)
    else:
        for i in num_list:
            mul*=i
        answer =mul
    return answer