n=input()

zero=0
one=0

for i in range(len(n)):
    if n[i-1]!=n[i]:
         if n[i]=='0':
             zero+=1
         elif n[i]=='1':
             one+=1
   
print(min(zero,one))
    