def solution(numbers, n):
    answer = 0
    for x in numbers:
        answer = answer + x
        if answer > n:
            break;
    return answer