from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]
    
    q = deque()
    q.append((0, 0, 1))
    
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while q:
        x, y, dist = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    maps[nx][ny] += maps[x][y]
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
    return -1
                
    
def solution(maps):
    return bfs(maps)