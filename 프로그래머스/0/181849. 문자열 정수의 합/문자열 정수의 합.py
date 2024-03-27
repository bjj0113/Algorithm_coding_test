def solution(num_str):
    answer = 0
    a = list(num_str)
    
    for i in a:
        answer += int(i)
    return answer