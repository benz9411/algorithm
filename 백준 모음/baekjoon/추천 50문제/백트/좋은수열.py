def dfs(depth,num):
    global exit_flag
    
    if exit_flag: #재귀 전체 종류 변수 체킹
        return
    
    if 1<= depth <= N:
        for j in range(len(num)-1): #마지마 전 변수까지
            for k in range(1,len(num)//2+1):
                if num[j:j+k]==num[j+k:j+2*k]: #만약 j부터 j+k까지와 j+k부터 j+2k까지의 배열이 동일하다면 
                    return #나쁜수열임
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

'''
 문제 골드 4이지만 파이썬의 슬라이싱 쓰면 인덱스가 범위를 넘어가는 부분을 고려하지 않아도 돼서 아주 쉽게 한줄로 풀 수 있다.  단, 인덱스를 고려하게 된다면 다음 밑의 if문에 인덱스가 넘어가는 부분을 다음과 같이 고려해야 한다. 

if len(num) >= 2 * k and j <= len(num) - 2 * k and num[j: j + k] == num[j + k:j + 2 * k]:

하지만 슬라이싱은 인덱스가 넘어가도 인덱스에러가 발생하지 않기 때문에 밑의 조건문 같이 구현해주면 쉽게 문제를 해결할 수 있다.

'''