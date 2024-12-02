import sys
input = sys.stdin.readline

def sol(x):
    if x in n_dict:
        return n_dict[x]
    else:
        return 0
        
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

n_dict = {x: 0 for x in n_list}

for num in n_list:
    n_dict[num] += 1

for x in m_list:
    print(f'{sol(x)} ',end="")