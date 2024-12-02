import sys
input = sys.stdin.readline

def sol(n):
    if n == 0 or n ==  1:
        return 2
    for num in range(n,n*n):
        if check(num):
            return num
        
        
def check(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
        
        
T = int(input())
for _ in range(T):
    n = int(input())
    print(sol(n))
            
