

while True:   
    leng=list(map(int,input().split()))
    if sum(leng)==0:
        break
    leng.sort()
    if (pow(leng[0],2)+pow(leng[1],2))==pow(leng[2],2):
        print('right')
    else:
        print('wrong')