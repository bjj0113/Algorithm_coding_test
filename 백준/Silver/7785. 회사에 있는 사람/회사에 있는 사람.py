import sys
input = sys.stdin.readline

n = int(input())
log = dict()
for _ in range(n):
    x = input()[:-6]
    if x in log:
        log.pop(x)
    else:
        log[x] = None
    
for name in sorted(log.keys(),reverse= True):
    print(name)