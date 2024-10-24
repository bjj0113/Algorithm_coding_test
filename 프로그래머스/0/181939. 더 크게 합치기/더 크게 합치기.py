def solution(a, b):
    answer = 0
    str1,str2 = '', ''
    
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    
    answer = int(max(str1,str2))
    return answer