k=int(input())

arr=[]
for i in range(k):
    sta=int(input())
    if sta!=0:
        arr.append(sta)
    else:
        arr.pop()
        
print(sum(arr))