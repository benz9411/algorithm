array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <=1:
        return array #퀵정렬 길이가 1이면 정렬이 다 된 뜻 return
    
    pivot=array[0]
    tail = array[1:] #피벗을 제외한 리스트
     #1차 피벗이 완료되면 왼쪽은 피벗 값보다 작고 오른쪽은 피벗보다 큼
    left_side = [x for x in tail if x<= pivot] 
    print("left_side=" ,left_side)
    right_side = [x for x in tail if x> pivot]
    print("r_side=" ,right_side)
    print("pivot =",pivot)
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#보통은 p(nlogn)의 복잡도를 가지지만 최악의 경우 O(N**2)의 시간 복잡도를 가짐
# 거의 정렬이 된 상태에 리스트의 경우임 여기서 삽입 정렬은 O(N)의 시간을 가짐