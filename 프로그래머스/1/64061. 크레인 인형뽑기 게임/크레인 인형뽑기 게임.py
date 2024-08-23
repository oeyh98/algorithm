
def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    
    def check():
        if len(stack) > 1 and stack[-1] == stack[-2]:
            print(stack)
            stack.pop()
            stack.pop()
            
            return 2
        return 0
        
        
    def crain(move):
        j = move - 1
        for i in range(n):
            if board[i][j] != 0:
                stack.append(board[i][j])       
                board[i][j] = 0
                return
        
    for move in moves:
        crain(move)
        answer += check()
        
    return answer