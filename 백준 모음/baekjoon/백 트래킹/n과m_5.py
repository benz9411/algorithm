n,m=map(int,input().split())

num=list(map(int,input().split()))
num.sort()
s=[]
print(num)
def back():
    print(s)
    if len(s)==m:
        return print(' '.join(map(str,s)))
        
    for i in range(len(num)):
        print(num[i])
        if num[i] not in s:
            s.append(num[i])
            back()
            s.pop
            
back()