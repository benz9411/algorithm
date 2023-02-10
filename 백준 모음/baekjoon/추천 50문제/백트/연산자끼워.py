n=int(input())
arr=list(map(int,input().split()))
a,s,m,d =map(int,input().split()) #덧셈, 뺄셈, 곱셈, 나눗셈
max_num=-1e9
min_num=1e9

def dfs(depth,num,add,sub,mul,div):
    global max_num,min_num
    if depth==n:
        max_num=max(num,max_num)
        min_num=min(num,min_num)
        return
    
    if add>0:
        dfs(depth+1,num+arr[depth],add-1,sub,mul,div)
    if sub>0:
        dfs(depth+1,num-arr[depth],add,sub-1,mul,div)
    if mul>0:
        dfs(depth+1,num*arr[depth],add,sub,mul-1,div)
    if div>0:
        dfs(depth+1,int(num/arr[depth]),add,sub,mul,div-1)
    
    
dfs(1,arr[0],a,s,m,d)    


print(max_num)
print(min_num)



