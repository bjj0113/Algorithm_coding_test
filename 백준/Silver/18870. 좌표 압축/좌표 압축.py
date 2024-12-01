import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))

ret = list()
setli = sorted(list(set(li)))

dic ={}
for i,k in enumerate(setli):
    dic[k] = i
    
for i in li:
    print(dic[i],end= " ")
    
