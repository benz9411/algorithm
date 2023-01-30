import sys
input=sys.stdin.readline
m,n=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(m)]
sum_data=[[0] * (m+1) for i in range(m+1)]

    
for i in range(1,m+1):
    for j in range(1,m+1):
        sum_data[i][j]=sum_data[i][j-1]+sum_data[i-1][j]-sum_data[i-1][j-1]+graph[i-1][j-1]


for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    
    print(sum_data[x2][y2]-sum_data[x1-1][y2]-sum_data[x2][y1-1]+sum_data[x1-1][y1-1])
