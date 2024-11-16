from collections import deque

def dfs(V):
    vdfs[V] = 1
    print(V, end = " ")
    for i in range(1,N+1):
        if not vdfs[i] and graph[V][i]:
            dfs(i)
    
def bfs(V):
    vbfs[V] = 1
    q = deque([V])
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in range(1, N+1):
            if not vbfs[i] and graph[V][i]:
                q.append(i)
                vbfs[i] = 1
    
    
N,M,V = map(int,input().split())

graph = [[0]* (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

vdfs = [0] * (N+1)
vbfs = [0] * (N+1) 
 
dfs(V)
print()
bfs(V)