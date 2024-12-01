
n = int(input())

li = list()
Len = list()
LenLi = [list() for _ in range(51)]
  

for _ in range(n):
    x = input()
    if len(x) not in Len:
        Len.append(int(len(x)))
    if x not in LenLi[len(x)]:
        LenLi[len(x)].append(x)
    
for i in Len:
    LenLi[i].sort()

for i in sorted(Len):
    for j in LenLi[i]:
        print(j)
        