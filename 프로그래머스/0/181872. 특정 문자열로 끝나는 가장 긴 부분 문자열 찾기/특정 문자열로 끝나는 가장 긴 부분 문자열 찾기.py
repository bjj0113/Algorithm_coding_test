def solution(myString, pat):
    answer = ''
    x = []
    
    for i,k in enumerate(myString):
        if myString[i:i+len(pat)] == pat:
            x.append(myString[:i+len(pat)])
    
    answer += max(x)
    return answer