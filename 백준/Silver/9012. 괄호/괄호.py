from collections import deque
import sys

input = sys.stdin.readline

def checkPS(Paren):
    
    for i in Paren:
        if not stack:
            if i == "(":
                stack.append(i)
            else:
                return False
        else:
            if stack[-1] == '(' and i == ")":
                stack.pop()
                continue
            stack.append(i)
    if stack:
        return False
    else:
        return True

for _ in range(int(input().strip())):
    stack = deque()
    Paren = input().strip()

    if checkPS(Paren):
        print("YES")
    else:
        print("NO")
                