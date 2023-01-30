n=1260
count=0

coin=[500,100,50,10]

for mo in coin:
    count+=n//mo
    n%=mo
    
    
print(count)