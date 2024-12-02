import sys
input = sys.stdin.readline

n, m = map(int,input().split())
Dogam = list()
for _ in range(n):
    Dogam.append(input().strip())
    
DictDogam = {poke: i for i,poke in enumerate(Dogam)}

for _ in range(m):
    ret = input().strip()
    if ret.isdigit():
        print(Dogam[int(ret)-1])
    else:
        print(DictDogam[ret]+1)
