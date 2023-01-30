num=int(input())
array=[]

for i in range(num):
    array.append(list(map(int,input().split())))

array=sorted(array,key=lambda x: (x[0],x[1]))


last=0
result=0

for i,j in array:
    if i>=last:
        result+=1
        last=j
    
print(result)  