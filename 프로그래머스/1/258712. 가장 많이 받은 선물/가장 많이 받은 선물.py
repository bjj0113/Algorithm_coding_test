def solution(friends, gifts):
    answer = 0
    sol = [0 for _ in range(len(friends))]
    present = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    # 주고받은 선물 표 만들기
    for x in gifts:
        g = x.split()
        give = friends.index(g[0])
        get = friends.index(g[1])
        present[give][get] += 1
    
    # 지수 표 만들기
    jisu = [[0 for _ in range(3)] for _ in range(len(friends))]
    
    for i in range(len(friends)):
        jisu[i][0] = sum(present[i]) # 준 선물
        for j in range(len(friends)):
            jisu[i][1] += present[j][i] # 받은 선물
        jisu[i][2] = jisu[i][0] - jisu[i][1]
    
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            else: 
                if present[i][j] - present[j][i] > 0 :
                    sol[i] += 1
                elif present[i][j] - present[j][i] == 0:
                    if jisu[i][2] > jisu[j][2]:
                        sol[i] += 1
                        
    answer = max(sol)
    return answer
