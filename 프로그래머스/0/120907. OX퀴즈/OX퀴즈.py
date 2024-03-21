def solution(quiz):
    answer = []
    op =0
    for i in quiz:
        l= []
        op = 0
        a = list(i.split(" "))
        
        for x in a:
            if(x == '-'):
                op = 1
            elif(x == '+'):
                op = 2
            else:
                l.append(x)
            
        if(op ==1):
            if(int(l[0])-int(l[1]) == int(l[3])):
                answer.append("O")
            else:
                answer.append("X")
        if(op ==2):
            if(int(l[0])+int(l[1]) == int(l[3])):
                answer.append("O")
            else:
                answer.append("X")
    return answer