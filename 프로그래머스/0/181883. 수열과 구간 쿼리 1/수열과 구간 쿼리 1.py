def solution(arr, queries):
    answer = arr[:]
    
    for j,s in enumerate(queries):
        for i in range(s[0],s[1]+1):
            answer[i] = answer[i]+1
    return answer