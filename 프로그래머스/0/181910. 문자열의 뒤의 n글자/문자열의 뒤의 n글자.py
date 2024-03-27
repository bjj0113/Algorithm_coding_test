def solution(my_string, n):
    answer = ''
    answer = my_string[-1:-n-1:-1]
    answer= answer[::-1]
    return answer