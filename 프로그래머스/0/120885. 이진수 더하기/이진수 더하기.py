def solution(bin1, bin2):
    answer = ''
    a = bin1
    b = bin2
    answer = bin(int(a,2) + int(b,2)).replace('0b','')
    
    return answer