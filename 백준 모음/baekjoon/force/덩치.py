


human=[]
n=int(input())
for i in range(n):
    human.append(list(map(int,input().split())))

# human=sorted(human,key=lambda x: (x[0],x[1]),reverse=True)

for i in range(n):
    count=1
    for j in range(n):
        if human[i][0]<human[j][0] and human[i][1]<human[j][1]: # 모든 경우가 크면
            count+=1
    print(count,end=' ')


            
         
    
         