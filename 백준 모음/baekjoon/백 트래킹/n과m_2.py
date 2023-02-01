m,n=map(int,input().split())
s=[]

def dfs(start):
    if len(s)==n:
        return print(' '.join(map(str,s)))
    
    for i in range(start,m+1):
        if not visited[i]:
            s.append(i)
            visited[i]=True
            dfs(i)
            s.pop()
            visited[i]=False 
            
    
    
    
visited =[False] * (m+1)

dfs(1)
