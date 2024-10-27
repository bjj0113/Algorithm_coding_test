def solution(my_string):
    answer = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for k in alpha:
        answer.append(my_string.count(k))
    return answer