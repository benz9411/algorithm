n,m=map(int,input().split())
num=list(map(int,input().split()))
#제약 = m을 넘지 않으면서 m과 최대한 가깝다

# 3장을 뽑는다 = 3중 for문으로 브루트 포스 생각
result=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum=num[i]+num[j]+num[k]
            if sum<=m:
                result.append(sum)

print(max(result))
