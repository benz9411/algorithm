n=int(input())

#n*n 체스판 위에 퀸 n개를 서로 공격할 수 없게 놓는다

arr=[[False]*n]*n

def dfs(x,y):
    if x<=1 or x>=n or y<=1 or y>=n: #체스판을 넘기지 않아야함
        return False
    
    if arr[x][y]==False:
        arr[x][y]==True
        dfs(x-1,y) #상
        dfs(x-1,y-1) # 대각선 왼쪽 위
        dfs(x,y-1) #좌
        dfs(x-1,y+1)
        dfs(x+1,y) #하
        dfs(x+1,y-1)
        dfs(x,y+1) # 우
        dfs(x+1,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1
print(result)
    
    