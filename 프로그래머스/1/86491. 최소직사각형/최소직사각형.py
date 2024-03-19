def solution(sizes):
    answer = 1
    a=[]
    b=[]
    for i in range(len(sizes)):
        a.append(sizes[i][0])
        b.append(sizes[i][1])
    
    for x in range(len(a)):
        if(a[x]>b[x]):
            temp = a[x]
            a[x] = b[x]
            b[x] = temp
    
    answer = max(a)* max(b)

    return answer

    