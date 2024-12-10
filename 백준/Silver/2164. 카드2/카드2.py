import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
deq = deque()
for i in range(1,n+1):
        deq.append(i)

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())
    
print(deq.pop())