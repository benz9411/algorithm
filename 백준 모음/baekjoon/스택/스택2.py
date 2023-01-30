num=int(input())
stack=[]
for i in range(num):
    a=input().split()
    if a[0]=='push':
        stack.append(int(a[1]))
    elif a[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif a[0]=='size':
        print(len(stack))
    elif a[0]=='pop':
         if stack:
             c=stack.pop()
             print(c)
         else:
             print(-1)
    elif a[0]=='empty':
        if stack:
            print(0)
        else:
            print(1)
        
        

