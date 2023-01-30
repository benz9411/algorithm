# 미로 탐색으로 보아 최소 거리 찾기
# 적은 효율성으로 bfs 적합
from collections import deque


n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
    
    
dx=[-1,1,0,0] #상 하 좌 우
dy=[0,0,-1,1]

# 1로 움직이고 0은 벽

def bfs(x,y):
    q=deque()
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            
            if nx>=n or nx<0 or ny>=m or ny<0:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    
    return graph[n-1][m-1] 
    
    
    
    
    
    
print(bfs(0,0))