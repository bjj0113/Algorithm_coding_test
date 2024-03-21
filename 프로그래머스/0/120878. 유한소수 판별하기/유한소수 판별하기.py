import math
def solution(a, b):
     
    y = b/math.gcd(a,b)
    
    while(y>1):
        if(y%2==0):
            y = y//2
        elif(y%5==0):
            y = y//5
        else:
            break
    if(y==1):
        return 1
    else:
        return 2