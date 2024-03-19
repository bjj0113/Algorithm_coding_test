def solution(emergency):
    answer = list(emergency)
    a = list(emergency)
    a.sort(reverse = True)
    for i in range(len(emergency)):
        answer[emergency.index(a[i])] = i+1
    return answer