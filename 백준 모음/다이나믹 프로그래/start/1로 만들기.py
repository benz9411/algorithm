num=int(input())

#1.x가 5로 나누어 지면 5로 나누기
#2.x가 3로 나누어 지면 3로 나누기
#3.x가 2로 나누어 지면 2로 나누기
#4.x에서 1을 빼기
result=0

while num>1:
    if num%5==0:
        num//=5
    elif num%3==0:
        num//=3
    elif num%2==0:
        num//=2
    else:
        num-=1
    print(num)
    result+=1

print(result)
# 내방식 + 그리디로 풀기는 다른 적절한 방법이 있는지 확인이 어렵다