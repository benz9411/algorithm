#M*N 체스판에서 8*8체스판을 만들예정 여기서 색칠해야 할거 최소값

# != 해서 COUNT 해야하고 + 8*8을 어디서 자를거냐 + 

n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))
    
color = []

for a in range(n-7):
    for b in range(m-7):
        indexW=0
        indexB=0
        for i in range(a,a+8): #잘랐으니 이제 8*8 만큼 브루트포스
            for j in range(b,b+8):
                if (i+j)%2 ==0:
                    if graph[i][j] !='W':
                        indexW+=1
                    if graph[i][j] !='B':
                        indexB+=1
                else:
                    if graph[i][j] !='B':
                        indexW+=1
                    if graph[i][j] !='W':
                        indexB+=1
        color.append(min(indexW,indexB))
        
print(min(color))
        