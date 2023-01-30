from collections import deque
def dfs(v):
    visited[v] = True

    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:  #visited[i]가 False때 재귀를 돌리는 의미 not 연산자
            dfs(i)

def bfs(start):
    q=deque()
    q.append(start)
    visited_bfs[start]=True
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i]=True   
    
n,m,start=map(int,input().split())

graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()   


visited=[False] * (n+1)
visited_bfs=[False] * (n+1)

dfs(start)
print()
bfs(start)


        
    


