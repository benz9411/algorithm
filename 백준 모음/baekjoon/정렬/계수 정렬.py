import sys
num=int(sys.stdin.readline())

arr=[0]*10001

for i in range(1,num+1):
    a=int(sys.stdin.readline())
    arr[a]+=1
    
for i in range(1,len(arr)):
    for j in range(arr[i]):
        print(i)
    
