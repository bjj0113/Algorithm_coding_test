def solution(n_str):
    strlist = list(n_str)
    
    for i in range(len(strlist)):
        if strlist[i] == "0":
            continue
        else:
            return n_str[i:]