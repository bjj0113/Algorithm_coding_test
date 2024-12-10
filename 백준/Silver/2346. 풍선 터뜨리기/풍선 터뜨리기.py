import sys, copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n  = int(input())
deq = deque(enumerate(map(int,input().split())))

seq = []
while deq:
    idx, p = deq.popleft()
    seq.append(idx +1)
    
    if p > 0 :
        deq.rotate(-(p - 1))
    else:
        deq.rotate(-p)
print(" ".join(map(str,seq)))

