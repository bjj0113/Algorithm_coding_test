def solution(my_string, m, c):
    answer = ''
    str1 = ''
    list1 = []
    a, b = 0,m
    for _ in range(len(my_string)//m):
        str1 = str1 + my_string[a:b]
        list1.append(str1)
        str1 = ''
        a = a+m
        b = b+m
    #print(list1)
    for y in list1:
        answer = answer + y[c-1]
    return answer