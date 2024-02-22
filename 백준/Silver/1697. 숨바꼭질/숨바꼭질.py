from collections import deque
n, k = map(int, input().split())
graph = [0] * 100001


def bfs(v):
    q = deque()
    q.append(v)
    graph[v] = 1

    while q:
        node = q.popleft()

        next_step = [node-1, node+1, node*2]

        for i in next_step:
            if 0 <= i < 100001:
                if graph[i] == 0:
                    graph[i] = graph[node] + 1
                    q.append(i)

            if i == k:
                return graph[i]


print(bfs(n)-1)
