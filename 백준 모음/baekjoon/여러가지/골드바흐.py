import math
num=10000
n=int(input())

array=[True for i in range(num+1)]
array[1]=0
for i in range(2,int(math.sqrt(num))+1):
        if array[i]==True:
            j=2
            while i*j<=num:
                array[i*j]=False
                j+=1

for i in range(n):
    inp=int(input()) #짝수 받기
    a=inp//2
    b=a
    while a>0:
        if array[a] and array[b]: # 둘 다 트루라면 즉 둘 다 소수라면
            print(a,b)
            break 
        
        else:
            a-=1
            b+=1
    
    

    
       
            
    
    
#두 소수중 차이가 가장 작은거 (앞에서 부터 해라)
# 합을 두 소수의 합으로 해야함 

# 진행 방향 permutation을 쓰면 결론으로 안감