def solution(number):
    answer = 0
    numlist = []
    
    for i in number:
        numlist.append(int(i))
    
    answer = sum(numlist)%9
    return answer