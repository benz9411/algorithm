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
    
def bfs(start):
    global cnt
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        v=q.popleft()
        visited[v]=True
        
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                cnt+=1
                visited[i]=True
            
print(graph)       
        
    
visited=[False]*(n+1)  
    

bfs(1)

print(cnt)