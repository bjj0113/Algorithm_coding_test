import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
que = deque()
for _ in range(n):
    x = list(map(str,input().split()))
    if x[0] == 'push':
        que.append(int(x[1]))
    elif x[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(que))
    elif x[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif x[0] == 'back':        
        if que:
            print(que[-1])
        else:
            print(-1)
