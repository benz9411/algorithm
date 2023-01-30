
n=int(input())

for i in range(n):
    h,w,p=map(int,input().split())
    cnt=p%h
    room=(p//h)+1
    if p%h==0: #배수라서 111넣으면 002 같이 이상한 값 나옴
        cnt=h
        room=p//h
    print(f'{cnt*100+room}')    