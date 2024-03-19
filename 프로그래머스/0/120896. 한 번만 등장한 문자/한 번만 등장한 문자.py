def solution(s):
    answer = ''
    for x in s: 
        if(s.count(x)==1):
            answer += x
        
    listan = list(answer)  
    listan.sort()
    answer = ''.join(listan)
    return answer