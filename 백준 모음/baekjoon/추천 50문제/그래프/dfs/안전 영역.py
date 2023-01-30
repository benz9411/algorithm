num=int(input())

graph=[]
cnt=0
for i in range(num):
    graph.append(list(map(int,input().split())))


def dfs(x,y):

    if x>=num or x<0 or y>=num or y<0:
        return False
    if graph[x][y]>5:
            graph[x][y]=0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True

    return False
    
result=0
a=[]
for i in range(num):
    for j in range(num): 
            if dfs(i,j)==True:
                    result+=1
   


            
print(result)