def solution(arr):
    answer = []
    answer += arr
    for i in range(11):
        if len(arr) <= 2**(i):
            x = 2**(i) - len(arr)
            for j in range(x):
                answer += [0]
            break
            
    
    
    return answer