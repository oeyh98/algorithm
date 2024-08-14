from heapq import heappush, heappop

INF = int(1e8)
n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    heapq = [(0, start)]
    distance[start] = 0

    while heapq:
        current_dist, current_node = heappop(heapq)

        if distance[current_node] < current_dist:
            continue

        for dest, weight in graph[current_node]:
            new_distance = weight + current_dist
            if new_distance < distance[dest]:
               distance[dest] = new_distance
               heappush(heapq, (new_distance, dest))

dijkstra(k)
for d in distance[1:]:
    print(d if d != INF else "INF")