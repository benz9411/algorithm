
def solution(board):
    max_len=len(board)
    #다시 말하지만 x,y는 좌표가 아닌 [x,y]라는걸
    dx=[-1,1,0,0,-1,1,1,-1] #상 하 좌 우
    dy=[0,0,-1,1,1,1,-1,-1]
    visited=[[False] *len(board) for _ in range(len(board))]
    

    def bfs(x,y):
        queue=deque()
        queue.append((x,y))
        while queue:
            x,y=queue.popleft()
            visited[x][y]=True
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<max_len and 0<=ny<max_len and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        queue.append((nx, ny))
                    else:
                        board[nx][ny] = 2 #위험지역 처리 
        
    for i in range(max_len):
        for j in range(max_len):
            if board[i][j]==1:
                bfs(i,j)
    result=0
    for i in board:
        result+=i.count(0)
    return result