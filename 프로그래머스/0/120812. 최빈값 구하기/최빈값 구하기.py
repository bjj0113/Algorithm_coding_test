def solution(array):
    answer = 0
    dic = dict.fromkeys(array)
    cnt = 0
    chk = 0 
    for x in dic:
        if(cnt<array.count(x)):
            cnt = array.count(x)
            answer = array[array.index(x)]
            chk =0
        elif(cnt == array.count(x)):
            chk =1
            
    if(chk ==1):
        return -1
    
    return answer