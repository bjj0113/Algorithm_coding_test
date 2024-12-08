from collections import deque
import sys

input = sys.stdin.readline

stk = deque()
for _ in range(int(input().strip())):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        stk.append(cmd[1])
        
    elif cmd[0] == 2:
        if stk:
            print(stk.pop())
        else:
            print(-1)
            
    elif cmd[0] == 3:
        print(len(stk))
        
    elif cmd[0] == 4:
        if not stk:
            print(1)
        else:
            print(0)
            
    elif cmd[0] == 5:
        if stk:
            print(stk[-1])
        else:
            print(-1)