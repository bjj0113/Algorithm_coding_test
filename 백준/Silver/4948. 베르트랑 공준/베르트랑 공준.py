import sys
input = sys.stdin.readline

n_list = [0] * (123456*2+1)
in_list = list()
while True:
    n = int(input())
    if n == 0:
        break
    else:
        in_list.append(n)


for i in range(2,123456*2+1):
    if n_list[i] == 0:
        for j in range(i+i,123456*2+1,i):
            n_list[j] = 1

for x in in_list:
    cnt = 0
    for y in range(x+1,2*x+1):
        if n_list[y] == 0:
            cnt += 1
    print(cnt)