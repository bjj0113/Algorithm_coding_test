import sys
input = sys.stdin.readline

n = int(input())
N = sorted(list(map(int,input().split())))
    
print(N[0]*N[-1])