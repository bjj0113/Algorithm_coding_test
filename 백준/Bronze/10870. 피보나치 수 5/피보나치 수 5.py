import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def sol(n):
    if n == 1 or n == 0:
        return n
    if n > 1:
        n = sol(n-1)+sol(n-2)
        return n

n = int(input().rstrip())

print(sol(n))