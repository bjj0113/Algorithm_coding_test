import sys
from collections import deque

N = int(sys.stdin.readline())

d = deque()
for _ in range(N):
    op = list(map(int, sys.stdin.readline().split()))
    
    if (op[0] == 1):
        d.appendleft(op[1])
    elif (op[0] == 2):
        d.append(op[1])
    elif (op[0] == 3):
        if (d):
            print(d.popleft())
        else:
            print(-1)
    elif (op[0] == 4):
        if (d):
            print(d.pop())
        else:
            print(-1)
    elif (op[0] == 5):
        print(len(d))
    elif (op[0] == 6):
        if (d):
            print(0)
        else:
            print(1)
    elif (op[0] == 7):
        if (d):
            print(d[0])
        else:
            print(-1)
    elif (op[0] == 8):
        if (d):
            print(d[-1])
        else:
            print(-1)