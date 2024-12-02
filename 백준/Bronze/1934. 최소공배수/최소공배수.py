import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def sol(a,b):
    num = a* b // gcd(a,b)
    
    return num
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    print(sol(a,b))
    