def solution(my_strings, parts):
    answer = ''
    
    for i,k in enumerate(my_strings):
        answer = answer + k[parts[i][0]:parts[i][1]+1]
    
    return answer