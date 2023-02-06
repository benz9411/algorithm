def dfs(depth,num):
    global exit_flag
    
    if exit_flag: #재귀 전체 종류 변수 체킹
        return
    
    if 1<= depth <= N:
        for j in range(len(num)-1): #마지마 전 변수까지
            for k in range(1,len(num)//2+1):
                if num[j:j+k]==num[j+k:j+2*k]:
                    return
    if depth==N: #종료조건
        print(num)
        exit_flag =True
        return
    
    for i in range(1,3+1):
        dfs(depth+1,num+str(i))






#1번째 좋은 수열을 발견할때 return 하는거 check 함수
#2번째 bfs()를 도는거 recursive 함수


N=int(input())
exit_flag=False
dfs(0,'')
