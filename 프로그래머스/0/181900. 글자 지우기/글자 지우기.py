def solution(my_string, indices):
    answer = ''
    a = list(my_string)
    for i in indices:
        a[i] = 0
    print(a)
    for _ in range(len(indices)):
        a.remove(0)
    answer = ''.join(a)
    return answer