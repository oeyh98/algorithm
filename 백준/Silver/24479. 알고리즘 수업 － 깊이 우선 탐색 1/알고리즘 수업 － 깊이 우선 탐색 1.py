import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node):
    global count
    count += 1
    visited[node] = count
    graph[node].sort()

    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)


dfs(r)
print(*visited[1:], sep='\n')
