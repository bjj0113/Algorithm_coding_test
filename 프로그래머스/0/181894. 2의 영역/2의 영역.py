def solution(arr):
    answer = []
    x,y = -1,-1
    for i,k in enumerate(arr):
        if k == 2:
            x = i
            break
    
    for i,k in enumerate(reversed(arr)):
         if k == 2:
            y = len(arr) - i 
            break
    answer = arr[x:y]
    
    if x == -1 :
        answer.append(-1)
    return answer