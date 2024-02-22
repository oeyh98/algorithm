from collections import deque
t = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(k, d):
    q = deque()
    q.append((k[0], k[1]))
    graph[k[1]][k[0]] = 1

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == d[0] and ny == d[1]:
                return graph[y][x] + 1

            if 0 <= nx < l and 0 <= ny < l:
                if visited[ny][nx]:
                    graph[ny][nx] = graph[y][x] + 1
                    visited[ny][nx] = False
                    q.append((nx, ny))


for _ in range(t):
    l = int(input())
    knight = list(map(int, input().split()))
    des = list(map(int, input().split()))
    graph = [[0] * l for _ in range(l)]
    visited = [[True] * l for _ in range(l)]

    if knight != des:
        print(bfs(knight, des)-1)
    else:
        print(0)
