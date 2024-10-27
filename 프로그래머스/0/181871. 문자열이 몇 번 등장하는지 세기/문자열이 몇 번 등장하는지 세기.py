def solution(myString, pat):
    answer = 0
    
    for i,k in enumerate(myString):
        if len(pat) > len(myString)-i:
            break
        else:
            j = i
        for l,m in enumerate(pat):
            if myString[j] == m:
                if l+1 == len(pat):
                    answer = answer + 1
                j = j + 1
            else:
                break
    return answer

