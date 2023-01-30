from itertools import combinations
a,b=map(int,input().split())

arr=[i for i in range(1,a+1)]

c=list(combinations(arr,b))



for i in c:
    print(' '.join(map(str, i)))