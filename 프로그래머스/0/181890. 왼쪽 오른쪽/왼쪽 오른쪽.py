def solution(str_list):
    answer = []
    for i, k in enumerate(str_list):
        if k == 'l':
            answer = str_list[:i]
            break
        elif k == 'r':
            answer = str_list[i+1:]
            break
            
    return answer