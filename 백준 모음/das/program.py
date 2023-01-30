from collections import deque

n,m,k,x=map(int,input().split()) # bfs 문제로 추정

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b) #이런 문제는 이 형식으로 받아야 1번에는 2,3 연결
    # 2번에는 뭐뭐 연결 이렇게 확인 가능
    
distance=[-1]*(n+1)
distance[x]=0 #시작 노드는 0으로

q=deque([x])
while q:
    now = q.popleft # 방문했으니 큐에서 뺸다
    for next_node in graph[now]: #현재 도시에서 이동할 수 있는 도시 확인
        if distance[next_node]==-1: #방문하지 않았으면   
            distance[next_node]=distance[now]+1 #최단 거리 갱신
            q.append(next_node)
            print(distance)

check = False
for i in range(1,n+1):
    if distance[i]==k: # 지문에서 원하는 값 2번 걸처갔나라는 뜨,ㅅ
        print(i)
        ckeck=True

if  check==False:
    print(-1)