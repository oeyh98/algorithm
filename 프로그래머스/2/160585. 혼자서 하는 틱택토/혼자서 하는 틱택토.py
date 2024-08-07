def is_over(board, player):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == player) or (board[0][i] == board[1][i] == board[2][i] == player):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True

    return False

def solution(board):
    b = ''.join(board) 
    o_cnt = b.count('O')
    x_cnt = b.count('X')
    
    # ox_cnt = o_cnt - x_cnt
    if o_cnt < x_cnt or o_cnt - x_cnt > 1:
        return 0
    
    o_result = is_over(board, "O")
    x_result = is_over(board, "X")
    
    if o_result:
        if (o_cnt - x_cnt != 1) or  x_result:
            return 0
            
    elif x_result:
        if o_cnt - x_cnt != 0:
            return 0
    
    return 1

