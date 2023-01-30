
n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
 
cnt=0   

def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n: #주어진 범위를 벗어나는 경우 즉시 종료
        return False
    if graph[x][y] ==1: 
        # 조건이 맞다면 방문 했으니 처리 해야 한다
        cnt+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        
        # 여기서 재귀함수는 return을 하지 않는다 graph[x][y]==1 방문 처리 재귀함수
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
grp.sort()
for i in grp:
    print(i)
    