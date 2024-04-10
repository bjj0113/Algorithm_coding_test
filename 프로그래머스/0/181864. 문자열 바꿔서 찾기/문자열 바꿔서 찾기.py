def solution(myString, pat):
    answer = 0
    x = pat.replace("A","b")
    y = x.replace("B","a")
    
    z = y.upper()
    if z in myString:
        answer =1
    return answer