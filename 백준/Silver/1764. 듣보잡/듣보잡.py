import sys
input = sys.stdin.readline

n, m = map(int,input().split())

hear = set()
for _ in range(n):
    hear.add(input().strip())

cnt = 0
ret = list()
for _ in range(m):
    seeAtom = input().strip()
    if seeAtom in hear:
        cnt += 1
        ret.append(seeAtom)
        
print(cnt)
for x in sorted(ret):
    print(x)