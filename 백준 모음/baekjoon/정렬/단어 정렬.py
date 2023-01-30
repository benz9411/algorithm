n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

arr=list(set(arr))
arr.sort()    
arr=sorted(arr,key=lambda x:len(x))


for i in arr:
    print(i)