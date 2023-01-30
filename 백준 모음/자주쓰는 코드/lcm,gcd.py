import math

a,b=2,4

def gcd(a,b):
    #최대 공약수
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
    
def lcm(a,b):
    #최소 공배수
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            return i
        
        
print(gcd(a,b))
print(lcm(a,b))

    # gcd_num=0
    # for i in range(min(denom1,denom2),2,-1):
    #     if denom1%i==0 and denom2%i==0:
    #         gcd_num=i
    #         break
    # print(lcm_num,gcd_num)
    
p