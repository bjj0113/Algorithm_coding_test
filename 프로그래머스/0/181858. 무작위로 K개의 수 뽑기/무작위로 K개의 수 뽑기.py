def solution(arr, k):
    answer = []
    for i in arr:
        if i in answer:
            continue
        elif i not in answer and len(answer) < k:
            answer.append(i)
    
    while len(answer) < k:
        answer.append(-1)
    return answer