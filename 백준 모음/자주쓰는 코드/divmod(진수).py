def solution(n,q):
    rev_base=''
    
    while n>0:
        n,mod =divmod(n,q)
        rev_base+=str(mod)
        
    
    return rev_base[::-1]
#역수인 진수를 뒤집어 줘야 원래 수가 나온다

print(solution(4,2))


print(format(42,'b'))