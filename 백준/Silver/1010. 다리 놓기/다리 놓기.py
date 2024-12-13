import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sol(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * sol(n-1)

for _ in range(int(input().rstrip())):
    n,k = map(int,input().split())

    print(sol(k)//(sol(n)*(sol(k-n))))