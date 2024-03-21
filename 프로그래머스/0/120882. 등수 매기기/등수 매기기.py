def solution(score):
    answer = []
    temp = []
    for x in range(len(score)):
        temp.append(sum(score[x]))
    temp2 =sorted(temp,reverse= True)
    
    for x in temp:
        answer.append(temp2.index(x)+1)
    return answer