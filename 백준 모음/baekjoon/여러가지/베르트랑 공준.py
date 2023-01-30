#n보다 크고 2n 보다 작거나 
import math

def prime(n2):
    array=[True for i in range(n2+1)]
    array[1]=0
    for i in range(2,int(math.sqrt(n2))+1):
        if array[i]==True:
            j=2
            while i*j<=n2:
                array[i*j]=False
                j+=1
            
    return array
        



while True:
    cnt=0
    n=int(input())
    if n==0:
        break

    n2=2*n
    array=prime(n2)
    for i in range(n+1,n2+1):
        if array[i]:
            cnt+=1
       
    print(cnt)

            

                        
    