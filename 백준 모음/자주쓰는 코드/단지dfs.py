#bfs queue에 넣어서 하는거
from collections import deque

n=int(input())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt=0
   
def dfs(x,y): #stack
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        cnt+=1
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        
        return True
    return False

grp=[]
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            grp.append(cnt)
            cnt=0
print(grp)
        