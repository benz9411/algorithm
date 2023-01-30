n,m=map(int,input().split())
num=list(map(int,input().split()))

#m과 가깝게 만들어야 한다

result=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a=num[i]+num[j]+num[k]
            if a<=m:
                result.append(a)
                
print(max(result))