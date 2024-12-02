import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    num = a* b // gcd(a,b)
    
    return num
def son(a,b,c,d):
    return a * lcm(b,d) // b + c * lcm(b,d) // d

a,b = map(int,input().split())
c,d = map(int,input().split())

print(f'{son(a,b,c,d)//gcd(son(a,b,c,d),lcm(b,d))} {lcm(b,d)//gcd(son(a,b,c,d),lcm(b,d))}',end= "")
    