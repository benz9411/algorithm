import sys
input=sys.stdin.readline
n,m=map(int,input().split())

name=dict()

for i in range(n):
    c=input().rstrip()
    name[c]=0 #중복이 없다 했으니 value는 0으로 다 집어넣음
cnt=0
new=[]
for _ in range(m):
    c=input().rstrip()
    if c in name:
        cnt+=1 # 딕셔너리 안에 있으면 듣도보도 못한 사람 (문제 해결 부분)
        new.append(c) 

print(cnt)
new.sort()
for i in new:# 사전 순으로 정렬하고 출력
    print(i)
        
        
    
