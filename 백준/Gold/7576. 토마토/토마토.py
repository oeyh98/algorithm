from collections import deque
#가로, 세로
m, n = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

for _ in range(n):
    graph.append(list(map(int, input().split(' '))))


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((j, i))
bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()

print(max(map(max, graph)) -1)