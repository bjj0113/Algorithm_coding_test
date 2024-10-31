def solution(answers):
    answer = []
    
    sol1 = [1,2,3,4,5]
    sol2 = [2,1,2,3,2,4,2,5]
    sol3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [-1,0,0,0]
    
    for i,k in enumerate(answers):
        if sol1[i%5] == k:
            cnt[1] +=1
        if sol2[i%8] == k:
            cnt[2] +=1
        if sol3[i%10] == k:
            cnt[3] +=1
            
    m = -1      
    for i in range(1,4):
        if cnt[i] >= m:
            m = cnt[i]
            
    for i in range(1,4):
        if cnt[i] == m:
            answer.append(i)
   
    return sorted(answer)