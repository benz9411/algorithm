#괴물이 있으면 0 괴물이 없으면 1 1로 가야하는 미로찾기 여기서 최소 칸 구하기
#탐색문제 뭐가 있으면 지나갔던 길을 돌아가야한다
#나의 위치에서 가장 가까운 노드 방문, 미로탐색->최단거리만으로 가지고 탈출

from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
    
#좌표가 나오면 선언해 두는게 좋은 느낌
dx=[-1,1,0,0] #상 하 좌 우
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y)) 
    while queue: #각 가까운 노드를 방문하기 때문에 없어지면 다 방문한거임
        x,y=queue.popleft()
        for i in range(4): #현재 위치에서 4방향 확인
            nx=x+dx[i]
            ny=y+dy[i]
            # 새로운 좌표에 관해서 
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1: # 미로를 지나갈 수 있는 길일때
                graph[nx][ny]=graph[x][y]+1 #문제처럼 처음은 1->2->3 처럼 더하는중
                # 결국 이거에 마지막 정수가 최단거리가 된다
                queue.append((nx,ny)) #마무리 후 새로운 (nx,ny) 좌표 반환
        #마지막 거리에 오면 넣을 nx ny이가 없어서 return 돰
    return graph[n-1][m-1]#의 값은 최단거리의 더한값이 출력된다
    
    
print(bfs(0,0)) #여기서 좌표는 1,1이지만 리스트구조는 0,0으로 시작한다