n=int(input())
num=list(map(int,input().split()))

result,explore=[],[]


def dfs():
    if len(explore)==n:
        sum=0
        for i in range(n-1):
             ab=abs(explore[i]-explore[i+1])
             sum+=ab
        return result.append(sum)
    
    for i in range(n):
        if not visited[i]:
            explore.append(num[i])
            visited[i]=True
            dfs()
            explore.pop()
            visited[i]=False
    
    
visited=[False]*(n+1)    
dfs()       

print(max(result))



