#퀵 정렬에서는 피벗이 사용된다. 교환하기 위한 '기준'을 바로 피벗이라 한다.
#가장 대표적인 분할 방식인 호어 분할 방식을 기준으로 퀵 정렬을 설명한다.

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start #피벗(기준)을 첫 번째 원소로 정한다.
    left = start+1 # 피벗 왼쪽(큰걸 찾는)건 시작 지점에서 +1한 위치
    right = end
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때 까지 반복
        while left<=end and array[left]<= array[pivot]:
            left+=1 #left를 더해주는 이유는 큰 데이터를 발견할때 while 문 종
            # 그 left 값이 피벗보다 큰 숫자 위치를 말한다
        while right > start and array[right] >= array[pivot]: #여기는 작은 데이터를 찾는
            right-=1
        if left > right: #왼쪽이 오른쪽 보다 클려면 엇갈려야함 , 작은 데이터와 피벗 교체
            array[right],array[pivot]=array[pivot],array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
    
quick_sort(array,0,len(array)-1)
print(array)
            
    