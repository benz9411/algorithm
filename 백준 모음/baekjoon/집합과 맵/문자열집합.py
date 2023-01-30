n,m=map(int,input().split())

s=dict()
for i in range(n):
    a=input()
    s[a]=1
cnt=0
for i in range(m):
    array=input()
    if array in s.keys():
        cnt+=1
        
print(cnt)
    
    