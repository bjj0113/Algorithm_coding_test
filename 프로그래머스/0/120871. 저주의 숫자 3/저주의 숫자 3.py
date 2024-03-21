def solution(n):
    y=0
    for _ in range(n):
        y+=1
        while("3" in str(y) or y%3 ==0):
            y+=1
    return y