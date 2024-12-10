import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
x = list(map(int,input().split()))
stack = [0]
cnt = 1

for i in x:

    if i == cnt:
        cnt +=1
    else:
        stack.append(i)
    while cnt == stack[-1]:
        cnt += 1
        stack.pop()
    
if cnt == n + 1:
    print("Nice")
else:
    print("Sad")