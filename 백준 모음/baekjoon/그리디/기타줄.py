n,m=map(int,input().split())

# m은 브랜드
#왼쪽은 패키지,오른쪽은 낱개 가격해서
# 가장 싸게 사는 방법

#그리디적 으로 n개를 가장 효율적인게 없이는 방식 거기다 최솟값
maker=[]
for i in range(m):
    maker.append(list(map(int,input().split())))

print(maker)