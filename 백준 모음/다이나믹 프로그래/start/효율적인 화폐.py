n,m = map(int,input().split())

array=[]

for i in range(n):
    array.append(int(input()))
    
# 한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001] * (m+1)
d[0]=0
for i in range(n): #몇 개의 동전에 따른 반복 시작
    # 만약 처음 시작이 2원이다
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j]=min(d[j],d[j-array[i]]+1)
            
if d[m]==10001:
    print(-1)
else:
    print(d[m])