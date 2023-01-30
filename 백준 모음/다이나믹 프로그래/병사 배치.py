#앞쪽이 있는 병사의 전투력이 항상 뒤쪽보다 높아야 한다

#특정한 위치에 있는 병사를 열외시킨다 병사수 최대
# 유의 열외 시켜야 하는 수를 출력해야 한다.
 
 # 가장 긴 증가하는 부분 수열
 #d[i] = array[i]
 #d[i]=max(d[i],d[j]+1)
 
x=int(input())
arr=list(map(int,input().split()))

dp=[1 for i in range(x)]

for i in range(1,x):
    for j in range(0,i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
            
print(max(dp))