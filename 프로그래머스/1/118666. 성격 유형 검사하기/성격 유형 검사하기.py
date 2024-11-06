def solution(survey, choices): # 3 2 1 0 1 2 3
    answer = ''
    result = [0,0,0,0]
    jipyop = ['R','C','J','A']
    jipyom = ['T','F','M','N']
    for i,cho in enumerate(choices):
        score = 0
        if cho > 4:
            x = survey[i][1]
            score = cho - 4
            if x in jipyop:
                result[jipyop.index(x)] += score
            else:
                result[jipyom.index(x)] -= score
        elif cho < 4:
            if cho == 1:
                score = 3
            elif cho == 2:
                score = 2
            else:
                score = 1
            x = survey[i][0] 
            if x in jipyop:
                result[jipyop.index(x)] += score
            else:
                result[jipyom.index(x)] -= score
    
    for i,r in enumerate(result):
        if r > 0:
            answer += jipyop[i]
        elif r < 0:
            answer += jipyom[i]
        else:
            answer += jipyop[i]
    return answer