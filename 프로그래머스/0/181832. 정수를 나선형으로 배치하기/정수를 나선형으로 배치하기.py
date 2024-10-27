def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    x,y = 0,0
    direc = 0
    cnt = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for i in range(n*n):
        answer[x][y] = cnt
        cnt += 1
        
        #다음위치
        nx, ny = x + dx[direc], y + dy[direc]
        
        #방향전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direc = (direc + 1) % 4
            #x,y 업데이트 전으로 돌아와서 새로운 방향으로 진행
            nx, ny = x + dx[direc], y + dy[direc]
        
        x,y = nx,ny
        
    return answer