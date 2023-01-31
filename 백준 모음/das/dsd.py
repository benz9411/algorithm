# 우선순위 큐

import heapq


h=[]
value=[2, 1, 3, 2]
for i in value:
    heapq.heappush(h,-i)

result=[]
for i in range(len(h)):
    print(-heapq.heappop(h))
    