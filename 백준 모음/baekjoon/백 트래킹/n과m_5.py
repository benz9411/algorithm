n,m=map(int,input().split())

num=list(map(int,input().split()))
num.sort()
s=[]
def back():
    if len(s)==m:
        return print(' '.join(map(str,s)))
    
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            s.append(num[i])
            back()
            s.pop()
            visited[i]=False
         

visited =[False] * (n+1)  
            
back()