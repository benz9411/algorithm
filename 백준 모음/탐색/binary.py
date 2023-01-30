def binary_search(array, target, start , end):
    if start > end:
        return None
    mid =(start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        # 찾는게 미드보다 작으니까 end가 mid가 되는 경우임
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    
n,target = list(map(int,input().split()))
array= list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
    
    
    
    