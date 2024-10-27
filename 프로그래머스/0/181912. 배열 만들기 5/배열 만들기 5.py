def solution(intStrs, k, s, l):
    answer = []
    
    for i,num in enumerate(intStrs):
        y= ''
        index = s
        for x in range(l):
            y += num[index]
            index += 1
        if int(y) > k:
            answer.append(int(y))
    return answer