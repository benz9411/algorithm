from collections import deque
import copy
import sys
input = sys.stdin.readline


n,m=map(int,input().split())

graph=[]
answer=0

for i in range(n):
    graph.append(list(map(int,input().split())))
    
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]
# wall 설치법의 백트리킹 법 다시한번 생각하고 나중에 실행해보기
def wall_con(cnt):
    if cnt==3:
        bfs() #조건대로 벽 3개를 세우면 bfs() 시작
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall_con(cnt+1)
                graph[i][j]=0 #방문하면 다시 돌리는거 마냥 새로운 조합을 위해 0으로 바꾼다

               
def bfs():
    global answer
    new_graph = copy.deepcopy(graph) #
    queue=deque()
    for i in range(n):
        for j in range(m):
            if new_graph[i][j]==2:
                queue.append((i,j))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if new_graph[nx][ny]==1:
                continue
            if new_graph[nx][ny]==0:
                new_graph[nx][ny]=2
                queue.append((nx,ny))
    zone=0
    for row in new_graph:
        zone+=row.count(0)
    answer=max(answer,zone)

wall_con(0)
print(answer)
               
            