n,m=map(int,input().split())


s=[]
def dfs():
    if len(s)==m:
        return print(s)
    
    for i in range(1,n+1):
        if i not in s: # 여기서 고민하지 못한점 for 문을 사용하면 됨
            s.append(i)
            dfs()
            s.pop()
        
    
    
dfs()


# 재귀버전

visited=[False] * (n+1)

def dfs2(num):
    if num == m:
        return
    
    for i in range(1,n+1):
        if visited[i]== False:
            visited[i]=True
            s.append(i)
            dfs(i+1)
            visited[i]=False
            s.pop()
            
dfs2(0)
        



