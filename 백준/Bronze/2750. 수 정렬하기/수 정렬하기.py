
x = list()
n = int(input())
for _ in range(n):
    x.append(int(input()))

for i in range(n-1):
    for j in range(i+1,n):
        if x[i]>x[j]:
            x[i], x[j] = x[j], x[i]

for a in x:
    print(a)