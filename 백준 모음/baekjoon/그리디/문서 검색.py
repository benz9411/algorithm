string=input()
find=input()


c=string.replace(find,'*') #이런 문자열 문제는 replace 생각하기

cnt=0
for i in c:
    if i == '*':
        cnt+=1
        
print(cnt)

