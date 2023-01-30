n,m=map(int,input().split())
num=list(map(int,input().split()))

result,explore=[],[]

def dfs(start):
    if len(explore)==3:
        su=sum(explore)
        if su<=m:
            result.append(su)
    for i in range(start,len(num)):
        if num[i] not in explore: 
            explore.append(num[i])
            dfs(i+1)
            explore.pop()
            
dfs(0)

print(max(result))
        
    
