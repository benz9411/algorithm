INF=1e9

#노드의 개수 및 간선의 개수를 입력받기
n=int(input())
m=int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
            
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c #a에서 b가는 비용을 c라고 설정
    
#점화식에 따리 min(D(ab),D(ak)+D(kb))
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('도달 x')
        else:
            print(graph[a][b], end='')
    print()
            