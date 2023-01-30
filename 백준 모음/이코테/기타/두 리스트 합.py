n,m=3,4

a=[1,3,5]
b=[2,4,6,8]

# 정렬된 두 리스트 합집합
result=[0]*(n+m)
i=0 #a가르킬 놈
j=0 #b 가르킬 놈
k=0 #result 가르킬놈

while i<n or j<m:
    #리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j >=m or (i<n and a[i]<=b[j]):
        result[k]=a[i]
        i+=1
    else:
        result[k]=b[j]
        j+=1
    k+=1

for i in result:
    print(i,end=' ')