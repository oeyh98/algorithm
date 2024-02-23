from collections import deque
#가로, 세로, 높이
m, n, h = map(int, input().split())
graph = []

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()
day = 0

for i in range(h):
    tmp = []
    for j in range(n):
        lst = list(map(int, input().split()))
        for k in range(m):
            if lst[k] == 1:
                q.append((k, j, i))
        tmp.append(lst)
    graph.append(tmp)


def bfs():
    global day
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nx, ny, nz))
                if day < graph[z][y][x]:
                    day = graph[z][y][x] - 1


bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()

print(day)
