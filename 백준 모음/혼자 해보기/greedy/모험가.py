m=int(input())

N=list(map(int,input().split()))

N.sort()

result=0
count=0

for i in N:
    count+=1
    if i<=count:
        result+=1
        count=0

print(result)