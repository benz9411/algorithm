i=1
while True:
    L,P,V=map(int,input().split())
    re=L+P+V
    if re==0:
        break
    
    a=V//P # 만약 20일 휴가에 8일중 연속이라면 16일은 써야함
    b=V%P # 그리고 남은 4일에 대한 나머지 값을 구한다.
    if b>L:
        b=L
    result= (a*L) + b# 그러면 8일중 5일이니까 a*L이 된다 그리고 나머지 확인
    print(f"Case {i}: {result}")
    i+=1