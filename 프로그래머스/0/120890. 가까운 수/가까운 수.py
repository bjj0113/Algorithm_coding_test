def solution(array, n):
    answer = 0
    a = []
    array.sort()
    for x in array:
        a.append(abs(n-x))
    answer = array[a.index(min(a))]
        
    return answer