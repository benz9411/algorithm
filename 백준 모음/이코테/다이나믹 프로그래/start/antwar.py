n=int(input())

array=list(map(int,input().split()))

#앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
d=[0] *100

#다이나믹 프로그래밍 진행 (보텀업)
d[0]=array[0] #첫 번째 에서 최대값을 얻는법 그대로 첫번째
d[1]=max(array[0],array[1]) # 두 번째 에서 최대값 얻는법 (0,1 번중 큰 값 가져오기)

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])
#점화식 = 어떤 수열의 각각의 항들의 관계를 나타낸 식


print(d[n-1])