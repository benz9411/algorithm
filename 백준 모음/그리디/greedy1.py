# n,m,k=map(int,input().split())

# lis = []
# lis=list(map(int,input().split()))


# lis.sort()
# first = lis[n-1]
# second = lis[n-2]
# result=0

# while True:
#     for i in range(k):
#         if m ==0:
#             break
#         result+=first
#         m-=1
#     if m==0:
#         break
#     result += second
#     m-=1
    
# print(result)
        
#수학적 알고리즘
# 6 6 6 5  k=3 할때 
# k+1 개의 수열 반복이 생긴다. 
# if m의 갯수가 k+1개로 안나눠지는 경우도 있으니
# int(m/(k+1)*k+m%(k+1))

# 결국은 가장 중요한거 이 사이클에 큰 수가 몇 번 더해지는 지를 구하는거다
# 위 예시는 6+6+6 6+6+6 이라는 큰 수가 6번

n,m,k=map(int,input().split())

lis = []
lis=list(map(int,input().split()))

lis.sort()
first = lis[n-1]
second = lis[n-2]

count = int(m/(k+1)*k)
count+= m%(k+1)

result=0
result += count * first
result += (m-count) *second

print(result)