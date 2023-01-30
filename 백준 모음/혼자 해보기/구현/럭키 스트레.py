s=input()

first=s[:len(s)//2]

second=s[len(s)//2:]
a,b=0,0
for i,j in zip(first,second):
    a+=int(i)
    b+=int(j)
    
if a==b:
    print('LUCKY')
else:
    print('READY')