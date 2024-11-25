def sol(n):
    for x in range(n):
        ret = sum(int(digit) for digit in str(x))
        if n == x + ret:
            return x
    
    return 0

n = int(input())
print(sol(n))