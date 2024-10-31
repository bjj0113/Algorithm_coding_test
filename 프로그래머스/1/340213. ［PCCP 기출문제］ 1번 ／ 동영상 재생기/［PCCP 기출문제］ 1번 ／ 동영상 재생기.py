def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    mm,ss = map(int,pos.split(':'))
    end_mm, end_ss = map(int, video_len.split(":"))
    op_start_mm, op_start_ss = map(int, op_start.split(":"))	
    op_end_mm, op_end_ss = map(int, op_end.split(":"))	
    
    if (op_start_mm<mm==op_end_mm and ss<op_end_ss) or \
        (op_start_mm<mm<op_end_mm) or \
        (op_start_mm==mm==op_end_mm and op_start_ss<=ss<op_end_ss) or \
        (op_start_mm==mm<op_end_mm and op_start_ss<=ss):
            mm, ss = op_end_mm, op_end_ss

    for com in commands:
        if com == 'next':
            if (end_mm == mm and end_ss - ss < 10) or (end_mm - 1 == mm and end_ss + 60 - ss < 10):
                mm, ss = end_mm, end_ss
            else:
                ss = ss + 10
                if ss >= 60:
                    mm += 1
                    ss -= 60
        else:
            if mm == 0 and ss < 10:
                mm, ss = 0, 0
            else:
                ss = ss - 10
                if ss < 0:
                    mm -= 1
                    ss += 60        
        
        if (op_start_mm<mm==op_end_mm and ss<op_end_ss) or \
            (op_start_mm<mm<op_end_mm) or \
            (op_start_mm==mm==op_end_mm and op_start_ss<=ss<op_end_ss) or \
            (op_start_mm==mm<op_end_mm and op_start_ss<=ss):
                mm, ss = op_end_mm, op_end_ss
        
        
    if mm < 10:
        smm = '0'+ str(mm)
    else:
        smm = str(mm)
    if ss < 10:
        sss = '0' + str(ss)
    else:
        sss = str(ss)
    answer = smm + ':' + sss
    return answer