from collections import deque

def solution(board, h, w):
    answer = 0
    l = len(board)
    visited = [[False] * l for _ in range(l)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    

        
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]

        if (0 <= nx < l and 0 <= ny < l) and board[nx][ny] == board[h][w]:
            answer += 1
            
    return answer


