def solution(my_string, s, e):
    answer = ''
    x =  my_string[s:e+1]
    x = x[::-1]
    answer = my_string[:s] + x + my_string[e+1:]
    return answer