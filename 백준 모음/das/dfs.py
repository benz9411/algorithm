n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
cnt=0
def dfs(x,y): #상하좌우를 들리는 dfs를 만들어 보자 
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1: #내가 방문해야 한느 목표라면
        cnt+=1
        graph[x][y]==0 #방문 처리를 해주고
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
    
    
    
   
grp=[]   
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            grp.append(cnt)
            cnt=0
            
            
print(len(grp))