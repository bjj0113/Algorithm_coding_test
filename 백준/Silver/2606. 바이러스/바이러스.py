# 바이러스
def search(v):
    nodeset[v] = 1
    for i in arr[v]:
        if nodeset[i] == 0:
            search(i)

x = int(input())
edgen = int(input())

nodeset  = [0]*(x+1) #방문 확인 할 노드 생성
root = 1 # 시작이 늘 1번컴퓨터

arr =[[] for j in range(x+1)]

for i in range(edgen): #연결된 엣지 표시
     a,b = map(int, input().split())
     arr[a].append(b)
     arr[b].append(a)

search(root)

n = sum(nodeset) - 1
print(n)