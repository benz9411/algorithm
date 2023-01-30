n,k = map(int,input().split())
result=0

while True:
    #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target=(n//k)*k #결국 이과정에서 -1값 아니면 n이 나누어진 값이 그대로 나온다
    result +=(n-target) # 이 부분에서 따로 if 처리가 아닌 변수로 -1을 빼는 행동이 가능
    n=target
    
    if n<k:
        break
    result+=1
    n//=k
    
#마지막으로 남은 수에 대하여 1씩 빼기   
result +=(n-1)
print(result)


#이 방법을 시간하면 O(logN)으로 가능하다