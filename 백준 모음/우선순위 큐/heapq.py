import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value) #h라는 배열에 value값을 힙푸쉬한다
    for i in range(len(h)): #힙에 들어간 길이만큼
        result.append(heapq.heappop(h)) # 힙 pop을 h번 실행한다 여기서 최소힙이라 작은 순서대로 반환
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)