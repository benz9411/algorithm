from collections import deque
#dfs는 큐 구조

n=int(input())

graph=[]
result=[]

for i in range(n):
    graph.append(list(map(int,input().rstrip())))
dx=[0,0,-1,1]# 상 하 좌 우
dy=[-1,1,0,0]# 상 하 좌 우
dx_y=[-1,-1,1,1]
dy_x-=[-1,1,-1,1]
    
def bfs(graph,x,y):

    queue=deque()
    queue.append((x,y))
    graph[x][y]==0
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]  #좌표 처리 하고
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1: #내가 찾는거면
                graph[nx][ny]==0
                queue.append((nx,ny))
                cnt+=1
    print(cnt)        
    return cnt
                 
         
    
    
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(graph,i,j))

print(result)