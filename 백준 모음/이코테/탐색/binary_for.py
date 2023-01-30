def binary_search(array,target,start,end):
    while start <= end:
        mid=(start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:# 찾는 지점이 미드보다 작음
            end=mid-1
        else:
            start=mid+1
    return None

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))


result=binary_search(array,target,0,n-1) 
if result==None:
    print("원소가 존재하지 않음")
else:
    print(result+1)
    

# 이진 탐색은 o(logN) 즉 탐색범위가 2000만이 넘어가거나 , 처리해야 할 데이터 개수나 
# 값이 1000만 단위 이상으로 넘어갈때 유용