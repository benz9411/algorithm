from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    
    visited[i][j]=0 #첫 방문처리
    
    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            
            if (0<=nx<n) and (0<=ny<m) and visited[nx][ny]==-1:
                if graph[nx][ny]==0:
                    visited[nx][ny]=0
                if graph[nx][ny]==1: #방문 가능하면
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))
                
     
    
n,m = map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

visited=[[-1]*m for _ in range(n)]  

for i in range(n):
    for j in range(m):
        if graph[i][j]==2 and visited[i][j]==-1:
            bfs(i,j)
            
for i in range(n):
    for k in range(m):
        if graph[i][k] == 0:
            print(0, end= " ")
        else:
            print(visited[i][k], end = " ")
            
    print()