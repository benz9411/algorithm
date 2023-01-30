n=input()

num=int(n[0])

for i in n[1:]:
    if num ==0:
        num+=int(i)
    else:
        num*=int(i)
        
    
print(num)
    