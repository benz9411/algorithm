n=int(input())
result=0

for i in range(1,n+1):
    a=list(map(int,str(i))) #a=list(map(int,str(i))) 자리수가 다 들어가는거 확인
    result=i+sum(a)
    if result==n:
        print(i)
        break
    if i ==n:
        print(0)
