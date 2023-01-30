ingredient=[2, 1, 1, 2, 3, 1, 2, 3, 1]
ham='1231'
ingredient=list(map(str,ingredient))
answer="".join(ingredient)
result=0
    

    
while True:
    a=answer.replace(ham,'*')
    if '*' in a:
        result+=a.count('*')
        a=a.replace('*',"")
            
    else:
        break

print(result)