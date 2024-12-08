import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)
def dfs(r):
    global cnt 
    visited[r] = cnt
    cnt += 1
    for k in graph[r]:
        if visited[k] == 0:
            dfs(k)    
    
    
    
n,m,r = map(int,input().split())

graph = [[]for _ in range(n+1)]
visited =[0] * (n+1)
cnt = 1
for _ in range(m):
    x, y = map(int,input().split())
    
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(n+1):    
    graph[i].sort(reverse= True)
dfs(r)

for x in visited[1:]:
    print(x)