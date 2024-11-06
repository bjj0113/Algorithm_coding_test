def solution(food):
    answer = ''
    cnt = 1
    for x in food[1:]:
        if x%2 == 1:
            x = x-1
        answer += str(cnt) * (x//2)
        cnt +=1
        
    r = answer[::-1]
    answer += '0'
    answer += r
    return answer