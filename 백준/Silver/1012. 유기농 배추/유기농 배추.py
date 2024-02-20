import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []


def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if base[ny][nx] == 1:
                    result.append((x,y))
                    base[ny][nx] = 0
                    q.append((nx, ny))


for _ in range(t):
    m, n, k = map(int, input().split())
    base = [[0]*m for _ in range(n)]
    worm = 0

    for _ in range(k):
        a, b = map(int, input().split())
        base[b][a] = 1

    for i in range(n):
        for j in range(m):
            if base[i][j] == 1:
                base[i][j] = 0
                worm += 1
                bfs(j, i)

    print(worm)
