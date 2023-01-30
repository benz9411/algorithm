#bfs queue에 넣어서 하는거
from collections import deque

n=int(input())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


   
def bfs(graph,x,y): #막혀있으니까 0으로 바꾸면 될듯
    qeueu=deque()
    qeueu.append((x,y))
    graph[x][y]=0
    count=1
    while qeueu:
        #여기 bfs 실행
        x,y=qeueu.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                qeueu.append((nx,ny))
                count+=1
    return count
                
                
cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(graph,i,j))
            
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
        