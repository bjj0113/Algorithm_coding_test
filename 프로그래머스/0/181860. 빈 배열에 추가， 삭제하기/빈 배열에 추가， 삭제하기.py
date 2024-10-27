def solution(arr, flag):
    answer = []
    
    for i,x in enumerate(flag):
        if x == True:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
    print(answer)
    return answer