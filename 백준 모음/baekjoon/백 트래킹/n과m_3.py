
m,n=map(int,input().split())
s=[]

def dfs():
    if len(s)==n:
        return print(' '.join(map(str,s)))
    
    for i in range(1,m+1):
        if not visited[i]:
            s.append(i)
            dfs()
            s.pop()
            
    
    
    
visited =[False] * (m+1)
dfs()