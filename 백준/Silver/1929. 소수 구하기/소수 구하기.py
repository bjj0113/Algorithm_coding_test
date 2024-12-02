import sys
input = sys.stdin.readline

def sol(n,m):
    if n == 1:
        n=2
    for num in range(n,m+1):
        if check(num):
            ret.append(num)
        
        
def check(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
        
        
n, m = map(int,input().split())
ret = list()
sol(n,m)
for x in ret:
    print(x)
            
