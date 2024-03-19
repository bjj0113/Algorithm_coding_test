def solution(s):
    answer = 0
    a = s.split(' ')
    for i,x in enumerate(a):
        if(x.isalpha()):
             answer -= int(a[i-1])
        else:
            answer += int(x)
    return answer