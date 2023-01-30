#dfs는 스택 구조 

n=int(input())

graph=[]
result=[]
cnt=0
for i in range(n):
    graph.append(list(map(int,input())))
dx=[0,0,-1,1]# 상 하 좌 우
dy=[-1,1,0,0]# 상 하 좌 우
    
def dfs(x,y):
    global cnt
    if x>=n or x<=-1 or y>=n or y<=-1:
        return False
    if graph[x][y]==1: # 내가 찾아야 하는 수이면
        for i in range(4):
            graph[x][y]=0
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        cnt+=1
            
        return True
    return False
    

  
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result.append(cnt) #그냥 실행이 아닌 단지이기 떄문에 이런거
            cnt=0
print(len(result))
result.sort()
for i in result:
    print(i)