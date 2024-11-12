def sol(x,y,n):
    c = 0
    
    if x > n or y > n:
        return 0
    
    while x <= n and y <= n:
        if x < y:
            x += y
        else:
            y += x
        c += 1
    return c

a = int(input())
for t in range(a):
    x,y,n = map(int,input().split())
    print(sol(x,y,n))
