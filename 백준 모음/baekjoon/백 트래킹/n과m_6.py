n,m=map(int,input().split())

num=list(map(int,input().split()))
num.sort()
s=[]
def back(start):
    if len(s)==m:
        return print(' '.join(map(str,s)))
    
    for i in range(start,n):
        if not visited[i]: #i번쨰는 방문하지 않았다면
            visited[i]=True #방문처리하고
            s.append(num[i]) #방문한 값을 넣는다
            back(i+1) #재귀
            s.pop()
            visited[i]=False
         

visited =[False] * (n+1)  
            
back(0)