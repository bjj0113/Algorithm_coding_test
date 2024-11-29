
n = int(input())

li = list()
for x in range(n):
    li.append(list(map(int,input().split())))

for a in sorted(li):
    for b in a:
        print(b,end= " ")
    print()