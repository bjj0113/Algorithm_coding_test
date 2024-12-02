import sys
input = sys.stdin.readline

T = int(input())
tc_list = list()
z_list = list()


prime_list = [0 for _ in range(1000001)]
prime_list[0] = prime_list[1] = 1

for i in range(2,1000001):
    if prime_list[i] == 0:
        z_list.append(i)
        for j in range(i+i,1000001,i):
            prime_list[j] = 1
                    
for _ in range(T):
    n = int(input())
    cnt = 0 
  
    for i in z_list:
        if i >= n:
            break
        if prime_list[n-i] == 0 and i <= n-i:
            cnt += 1
    
    print(cnt)
