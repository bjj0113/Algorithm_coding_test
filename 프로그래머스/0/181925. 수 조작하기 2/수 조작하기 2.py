def solution(numLog):
    answer = ''
    dic = {1:'w', -1:'s',10:'d',-10:'a' }
    list1 = []
    for i,k in enumerate(numLog):
        if(i+1 == len(numLog)):
            break
        list1.append(numLog[i+1]-k)
    
    for i,k in enumerate(list1):
        answer = answer + dic[k]
    return answer