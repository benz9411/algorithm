# 전체 범위 찾는거니까  bfs가 좋다고 생각
from collections import deque
n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt=0

def dfs(start):
    global cnt
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            visited[i]=True
            dfs(i)
            cnt+=1
            # visited[i]=False   
        
    
visited=[False]*(n+1)  
    

dfs(1)

print(cnt)