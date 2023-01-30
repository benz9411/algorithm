import math
n,m=map(int,input().split())
array=[True for i in range(m+1)]
array[1]=0
for i in range(2,int(math.sqrt(m))+1):
    if array[i]==True: #i가 소수인 경우
        j=2
        while i*j <=m:
            array[i*j]=False
            j+=1
            
for i in range(n,m+1):
    if array[i]:
        print(i)
        