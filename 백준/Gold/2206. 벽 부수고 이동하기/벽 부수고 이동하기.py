from collections import deque
n, m = map(int,input().split())

graph = []
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == m-1 and y == n-1 :
            return visit[y][x][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visit[ny][nx][z] == 0:
                    if graph[ny][nx] == 0:
                        q.append((nx, ny, z))
                        visit[ny][nx][z] = visit[y][x][z] + 1
                    else:
                        if z == 0:
                            q.append((nx, ny, 1))
                            visit[ny][nx][1] = visit[y][x][z] + 1
    return -1

print(bfs())
#print(visit)

