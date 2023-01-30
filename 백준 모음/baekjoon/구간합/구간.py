import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

per_fix = [0]
sum=0
for i in a:
    sum+=i
    per_fix.append(sum)
a=[]
for _ in range(m):
    b,c=map(int,input().split())
    a.append(per_fix[c]-per_fix[b-1])

for i in a:
    print(i)