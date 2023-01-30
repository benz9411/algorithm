num=int(input())
array=[]

for i in range(num):
    array.append(list(map(int,input().split())))

array=sorted(array,key=lambda x: (x[1],x[0]))


for i,j in array:
    print(i,j)

# N=int(input())
# arr=[]
# for i in range(N):
#     a,b = map(int,input().split())
#     arr.append((a,b))
# arr.sort()
# for i in range(N):
#     print(arr[i][0],arr[i][1])