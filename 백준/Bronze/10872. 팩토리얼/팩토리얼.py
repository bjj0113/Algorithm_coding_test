import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sol(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * sol(n-1)


n = int(input().rstrip())

print(sol(n))