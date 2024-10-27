def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        x = []
        for i in arr[s:e+1]:
            if i > k:
                x.append(i)
        if not x:
            answer.append(-1)
        else:
            answer.append(min(x))
        
    return answer