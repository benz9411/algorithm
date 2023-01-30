n,m = map(int, input().split())
visited=[False] * (n+1)
s=[]

def dfs():
    if len(s) ==m:
         print(' '.join(map(str,s)))
        #  print(list(map(str,s)))
         return  # dfs 재귀 함수를 끝내는 조건
    for i in range(1,n+1):
        if not visited[i]: # False 이면
            visited[i]=True # 방문 처리를 해주고
            s.append(i) # i값을 넣어주고
            # print(s,'append')
            dfs()
            s.pop()
            # print(s,'pop')
            visited[i]=False



dfs()