
n = int(input())
person = list()
cnt = [[] for _ in range(201)] 


for i in range(n):
    age, name =  input().split()
    
    cnt[int(age)].append(name)

for i,k in enumerate(cnt):
    if cnt[i]:
        for x in cnt[i]:
            print(i, end= " ")
            print(x)
