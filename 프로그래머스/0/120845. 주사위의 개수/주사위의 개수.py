def solution(box, n):
    answer = 1
    for x in box:
        answer *= x//n
    return answer