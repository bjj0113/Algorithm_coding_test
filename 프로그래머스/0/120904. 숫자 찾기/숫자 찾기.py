def solution(num, k):
    a = str(num)
    x = a.find(str(k))
    if(x != -1):
        return x+1
    else:
        return -1
