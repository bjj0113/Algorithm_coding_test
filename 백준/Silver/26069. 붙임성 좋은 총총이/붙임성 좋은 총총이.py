import sys
input = sys.stdin.readline

n = int(input().rstrip())
txt = dict()
cnt = 0
for _ in range(n):
    a,b = input().split()
    if a not in txt :
        txt[a] = 0      
    if b not in txt:
        txt[b] = 0
        
    if a == "ChongChong" or b == "ChongChong":
        txt[a] = 1
        txt[b] = 1
        
    if txt[a] == 1 or txt[b] == 1:
        txt[a] = 1
        txt[b] = 1
for x in txt:
    if txt[x] == 1:
        cnt += 1 
        
print(cnt)