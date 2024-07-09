def solution(num_list, n):
    answer = []
    for i,x in enumerate(num_list):
        if i >= n :
            answer.append(x)
    for i,x in enumerate(num_list):
        if i == n:
            break;
        answer.append(x)
    return answer