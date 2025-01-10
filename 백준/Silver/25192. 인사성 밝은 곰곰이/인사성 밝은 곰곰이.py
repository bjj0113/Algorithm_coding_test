import sys
input = sys.stdin.readline

n = int(input().rstrip())
txt = dict()
cnt = 0
for _ in range(n):
    x = input().rstrip()
    if x == "ENTER":
        txt.clear()
        
    elif x not in txt:
        txt[x] = 0
        cnt += 1
        
print(cnt)