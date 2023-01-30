num=int(input())
array=list(map(int,input().split()))

li=[]
for i in range(num):
    count=0
    for j in range(num):
        if array[i]>array[j]:
            count+=1
    li.append(count)
    
for i in li:
    print(i,end=' ')