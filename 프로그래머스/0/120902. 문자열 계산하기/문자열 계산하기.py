def solution(my_string):
    answer = 0
    a = my_string.split()
    numstack = []
    opstack = []
    i =0
    j = 0
    for x in a:
        if(x.isdigit()):
            numstack.append(x)
        else:
            opstack.append(x)
    i = int(numstack[0])
    op = opstack[0]
    
    while(1):
        del numstack[0]
        j = int(numstack[0])
        if(op == '+'):
            i = i+j
        else:
            i = i-j
        del opstack[0]
        if(len(opstack)==0):
            break
        op = opstack[0]
    answer = i
    return answer