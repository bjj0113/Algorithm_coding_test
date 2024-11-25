def sol(m,n,board):
    minret = float('inf')
    for x in range(m-8+1):
        for y in range(n-8+1):
            ret1,ret2 = 0,0
            for x1 in range(0,8,2):
                for y1 in range(0,8,2):
                    if board[x + x1][y + y1] != 'W':
                        ret1 +=1
                    if board[x + x1][y+ y1 + 1] != 'B':
                        ret1 +=1                    
                    if board[x + x1 +1][y+ y1] != 'B':
                        ret1 +=1
                    if board[x + x1 +1][y+ y1 + 1] != 'W':
                        ret1 +=1

            for x1 in range(0,8,2):
                for y1 in range(0,8,2):
                    if board[x + x1][y + y1] != 'B':
                        ret2 +=1
                    if board[x + x1][y+ y1 + 1] != 'W':
                        ret2 +=1
                    if board[x + x1 +1][y+ y1] != 'W':
                        ret2 +=1
                    if board[x + x1 +1][y+ y1 + 1] != 'B':
                        ret2 +=1

            if minret > min(ret1,ret2) :
                minret = min(ret1,ret2) 
           
    return minret

m,n = map(int,input().split())
board = list(list(input()) for _ in range(m))
print(sol(m,n,board))
