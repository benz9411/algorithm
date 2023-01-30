#정렬 알고리즘으로 데이터를 정렬하면 다음 장에서도 배울 이진 탐색 가능

#선택 정렬
# 가장 원시적인 방법으로 가장 작은 것 을 찾아서 앞으로(오름차순 기준)

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] < array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index], array[i] #swap
    
print(array)
    
    
#특정한 리스트에서 가장 작은 데이터를 찾을 때 좋을 수 있음