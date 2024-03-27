def solution(num_list, n):
    answer = []
    for i,v in enumerate(num_list):
        if i+1>=n:
            answer.append(v)
    return answer