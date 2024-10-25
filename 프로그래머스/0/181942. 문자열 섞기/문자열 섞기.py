def solution(str1, str2):
    answer = ''
    for i,k in enumerate(str1):
        answer += k
        answer += str2[i]
            
    
    return answer