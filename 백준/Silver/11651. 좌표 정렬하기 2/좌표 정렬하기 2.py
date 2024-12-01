
n = int(input())

li = list()
for x in range(n):
    ret = list(map(int,input().split()))
    li.append(list(reversed(ret)))

for a in sorted(li):
    for b in a[::-1]:
        print(b,end= " ")
    print()