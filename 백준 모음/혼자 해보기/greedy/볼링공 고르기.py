
n,m=map(int,input().split())

data=list(map(int,input().split()))

data.sort()

result=[]

for i in range(n):
    for j in range(i,n):
        if data[i] != data[j]:
            result.append((data[i],data[j]))
            
print(len(result))
