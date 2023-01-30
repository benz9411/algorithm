from collections import deque


n,m,k,x = map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split()) #내가 이걸 못했음
    graph[a].append(b)
    
    
distance = [-1] * (n+1)
distance[x]=0

#bfs 실행
q=deque([x]) #출발도시 x부터 시작

while q:
    now=q.popleft()
    for next_node in graph[now]:   # 처음 bfs 배울때 for 
                if distance[next_node]==-1:
                    distance[next_node]=distance[now]+1
                    q.append(next_node)

check=False

for i in range(1,n+1):
    if  distance[i]==k: #최단거리가 k와 같으면
        print(i)
        check=True
        
if not check:
    print(-1)
    
                    
                    
