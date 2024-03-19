def solution(array):
    answer = 0
    a =''
    for i in array:
        a += str(i)
    answer = a.count("7")
    return answer