def solution(babbling):
    answer = 0
    baby = ["aya","ye","woo","ma"]
    result=[]
    print(babbling)
    for x in babbling:
        for i in range(4):
            if(baby[i] in x):
                x =x.replace(baby[i],'-')
        x=x.replace('-','')
        if(x ==''):
            answer += 1
    
    return answer