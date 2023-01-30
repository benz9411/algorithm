array=[7,5,9,0,3,1,6,2,4,8]


for i in range(1,len(array)): #첫 번째 자리가 정렬되어 있다고 판단한다
    for j in range(i,0,-1):
        #여기서 j는 삽입하고자 하는 원소의 위치
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break
        
print(array)

#삽입 정렬ㄹ은 거의 정렬되어 있는 상태라면 매우 바르게 동작한다 o(n)까지 가능