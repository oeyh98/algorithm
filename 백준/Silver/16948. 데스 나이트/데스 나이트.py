from collections import deque

n = int(input())
graph = [[0]*n for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, +1, -2, +2, -1, +1]

r1, c1, r2, c2 = map(int, input().split())


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0

    while dq:
        x, y = dq.popleft()

        if x == r2 and y == c2:
            return graph[x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    dq.append((nx, ny))


result = bfs(r1, c1)
if result:
    print(result)
else:
    print(-1)