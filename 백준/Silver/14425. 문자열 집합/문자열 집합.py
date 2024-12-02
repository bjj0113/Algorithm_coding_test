import sys
input = sys.stdin.readline

n, m = map(int,input().split())
S = list()
test = list()
for _ in range(n):
    S.append(input())
for _ in range(m):
    test.append(input())

cnt = 0
for x in test:
    if x in S:
        cnt += 1
    
print(cnt)

