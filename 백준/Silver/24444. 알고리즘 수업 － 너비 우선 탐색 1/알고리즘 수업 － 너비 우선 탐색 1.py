import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
queue = deque()

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(r):
    global count
    count += 1
    visited[r] = count
    queue.append(r)

    while queue:
        node = queue.popleft()
        graph[node].sort()

        for g in graph[node]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                queue.append(g)



bfs(r)
print(*visited[1:], sep='\n')
