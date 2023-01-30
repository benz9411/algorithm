import sys
input=sys.stdin.readline
n,m=map(int,input().split())
pkm=dict() # 포켓몬 이름이 키 값인 딕셔너리
for i in range(1,n+1):
    name=input().rstrip()
    pkm[name]=str(i)

reverse_pkm=dict(map(reversed,pkm.items()))    #숫자가 키 값인 딕셔너리

for j in range(m):
    a=input().rstrip()
    if a.isdigit():
        print(reverse_pkm[a])
    else:
        print(pkm[a])


    

    

# 리스트로 처리하면 시간 존나 걸림
# 딕셔너리 사용해서 o(n) 시간으로 검색하기