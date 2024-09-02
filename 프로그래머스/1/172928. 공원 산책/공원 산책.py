def solution(park, routes):
    n, m = len(park), len(park[0])
    dx = {'N':-1, 'S':1, 'E':0, 'W': 0}
    dy = {'N': 0, 'S':0, 'E':1, 'W':-1}
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x = i
                y = j
    
    def check(x, y, dire, dist):
        for i in range(1, dist + 1):
            nx = x + (dx[dire] * i)
            ny = y + (dy[dire] * i)
            
            if not (0 <= nx < n and 0 <= ny < m) or park[nx][ny] == 'X':
                return (x, y)
                
    
        x += (dx[dire] * dist)
        y += (dy[dire] * dist)
        
        return (x, y)
            
        
    for route in routes:
        dire, dist = route.split(" ")
        x, y = check(x, y, dire, int(dist))
            
    
    return [x, y]