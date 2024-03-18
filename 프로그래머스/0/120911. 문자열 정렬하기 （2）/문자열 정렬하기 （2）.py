def solution(my_string):
    answer = ''
    x = list(my_string.lower())
    x.sort()
    answer = ''.join(x)
    return answer