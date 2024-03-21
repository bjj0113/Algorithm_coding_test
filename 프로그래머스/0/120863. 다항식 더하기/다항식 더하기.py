def solution(polynomial):
    answer = ''
    sumx,sumc =0,0
    py = polynomial.replace('+',' ')
    pyl = list(py.split())
    
    for x in pyl:
        if(x[-1] =='x'):
            if(x=='x'):
                sumx+=1
            else:
                sumx += int(x[0:-1])
        else:
            sumc += int(x)
    
    if(sumx == 0):
        answer = str(sumc)
    elif(sumc == 0):
        if(sumx == 1):
            answer = 'x'
        else:
            answer = str(sumx)+'x'
    elif(sumc == 0 and sumx == 0):
        answer = '0'
    else:
        if(sumx == 1):
            answer = 'x + '+str(sumc)
        else:
            answer = str(sumx)+'x + '+str(sumc)
    return answer