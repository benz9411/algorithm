n,m=map(int,input().split())

num=list(map(int,input().split()))
num.sort()
s=[]
def back():
    if len(s)==m:
        return print(' '.join(map(str,s)))
    
    for i in range(n):
        if not visited[i]:
            s.append(num[i])
            visited[num[i]]=True
            back()
            s.pop()
            visited[num[i]]=False
         

visited =[False] * (max(num)+1)  
            
back()