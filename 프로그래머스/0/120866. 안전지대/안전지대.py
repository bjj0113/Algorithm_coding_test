def solution(board):
    answer = 0
    dx = [-1, 1, 0, 0, -1, -1, 1, 1] 
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    inx =[]
    
    for x in range(len(board)):
        for y in range(len(board)):
            if(board[x][y] == 1):
                inx.append([x,y])
                
    for x,y in inx:
        for i in range(8):
            bx = x + dx[i]
            by = y + dy[i]
            if(0<=bx<len(board) and 0<=by<len(board)):
                board[bx][by] = 2
            
            
    for x in range(len(board)): 
        answer += board[x].count(0)
        
    print(answer)
    return answer