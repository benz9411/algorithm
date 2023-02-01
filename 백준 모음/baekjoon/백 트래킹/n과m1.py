n,m=map(int,input().split())

num=[4,5,2]
s=[]
def dfs():
    if len(s)==m:
       return print(" ".join(map(str,s)))
    
    for i in num:
        print(i,s)
        if i not in s:
            s.append(i)
            dfs()

            
            
dfs()



