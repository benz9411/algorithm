n,m = map(int,input().split())

result=0
for i in range(n):
    data=list(map(int,input().split()))
    mina = min(data)
    result = max(result,mina)
    
print(result)

# 가장 중요한건 -> 해결방식
# 각 행마다 작은수를 찾은 뒤에 그 수 중에서 가장 큰 수