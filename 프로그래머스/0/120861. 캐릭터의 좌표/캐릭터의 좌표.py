def solution(keyinput, board):
    answer = [board[0]//2,board[1]//2]
    direc = ["left","right","up","down"]
    
    for i in keyinput:
        if(i == direc[0] and answer[0]>0):
            answer[0] =answer[0]-1
        elif(i == direc[1] and answer[0] < board[0]-1):
            answer[0] =answer[0]+1
        elif(i == direc[2] and answer[1] < board[1]-1):
            answer[1] =answer[1]+1
        elif(i == direc[3] and answer[1]>0):
            answer[1] =answer[1]-1
            
    answer = [answer[0] - board[0]//2,answer[1] - board[1]//2]
    return answer