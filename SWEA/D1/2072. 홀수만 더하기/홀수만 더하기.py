
n = int(input())

for x in range(n):
    sumy = 0
    y = list(map(int,input().split()))
    for i in range(10):
    	if y[i]%2 == 1:
             sumy += y[i]
    print(f'#{x+1} ',end = "")
    print(sumy)