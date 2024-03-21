def solution(lines):
    
    answer = 0
    count = [0 for _ in range(200)] # -100 ~ 100 까지의 범위에서 해당 점에 선분이 그어진 횟수
    for line in lines:
        for i in range(line[0], line[1]): 
            count[i + 100] += 1 #-3,-1 경우 점 두개 찍음 0.5 지점에 점찍는다고 생각
    answer += count.count(2) # 두 개 이상 겹친 점
    answer += count.count(3) # 세 개 이상 겹친 점
    return answer