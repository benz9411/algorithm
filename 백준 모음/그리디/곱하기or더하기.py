data=input()
result=int(data[0])

# for i in s:
#     i=int(i)
#     if result==0:
#         result+=i
#         continue
    
#     if i<=1:
#         result+=i
#     else:
#         result*=i
        
#print(result)


for i in range(1,len(data)):
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*= num
        
print(result)