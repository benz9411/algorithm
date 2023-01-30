n,m=map(int,input().split())

a=list(map(int,input().split()))


per_fix=[]
per_fix.append(sum(a[:m])) # 첫 번째 합 등장

for i in range(n-m): #10 -2 =8 반복
  
    per_fix.append(per_fix[i]-a[i]+a[m+i])
    


        
    
print(max(per_fix))

# 수열 (구간 합 알고리즘중 접두사 합 알고리즘이 있고)
# 결국 이 알고리즘 핵심은 미리 합을 구해놓고 사용한다는 점이다/.