import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sol(T):
    isSmallOrBig = [0] # 현재 소괄호면 양수 / 대괄호면 음수
    for x in T:
        if x == '(':
            isSmallOrBig.append(1)
        if x == ')':   
            if isSmallOrBig.pop() <= 0:
                return False
            
        if x == '[':
            isSmallOrBig.append(-1)
        if x == "]":    
            if isSmallOrBig.pop() >= 0:
                return False
    if len(isSmallOrBig) > 1:
        return False
    return True
    
while True:
    T = input().rstrip()
    if T == ".":
        break
    
    if sol(T):
        print('yes')
    else:
        print('no')
        