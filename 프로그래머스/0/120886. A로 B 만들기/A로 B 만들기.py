def solution(before, after):
    answer = 0
    a = list(before)
    a.sort()
    b = list(after)
    b.sort()
    if(a == b):
        answer = 1
    else:
        answer = 0
    return answer