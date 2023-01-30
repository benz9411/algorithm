import heapq
from re import L
import sys

input=sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input()) #시작 노드 번호 입력받기
graph=[[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 리스트
distance=[INF]*9 #최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # a번 노드에 b번 노드로 가는 비용이 c라는 의미


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #시작 노드로 가기 위한 최단 경로는 0으로 설정,큐 삽입
    distance[start]=0
    while q: #큐가 비어있지 않으면
        #가장 최단 거리가 짧은 도으에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        if distance[now] <dist: #현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1] #
            #현재 노드를 거쳐서 , 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0])) 

dijkstra(start) #시작 지점에서 다익스트라 함수 시작


for i in range(1,n+1): #모든 노드로 가기 위한 최단 거리를 출력
    if distance[i] == INF:
        print('da')
    else:
        print(distance[i])