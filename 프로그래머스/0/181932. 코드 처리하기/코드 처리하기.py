
mode = 0

def changeMode():
    if mode == 0:
        mode = 1
    else: 
        mode = 0

    return mode

def solution(code):
    ret = ''
    mode = 0
    for i,k in enumerate(code):
        if mode == 0:
            if code[i] != '1' and i%2 ==0:
                ret += code[i]
            elif code[i] == '1':
                mode = 1
                
        elif mode == 1:
            if code[i] != '1' and i%2 ==1:
                ret += code[i]
            elif code[i] == '1':
                mode = 0
                
    if not ret:
        return "EMPTY"
    return ret