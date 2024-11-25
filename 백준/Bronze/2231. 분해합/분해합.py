def sol(n):
    num = list(map(int,str(n)))
    numlen = len(num)
 
    for x in range(10**numlen):
        if n == x + sum(list(map(int,str(x)))):
            return x
    
    return 0

n = int(input())
print(sol(n))