import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)
n, d = map(int, input().split())
graph = [[] for i in range(d+1)]
distance = [INF] * (d + 1)

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, dest, dist = map(int, input().split())
    if dest <= d:
        graph[start].append((dest, dist))

hq = []
distance[0] = 0
heappush(hq, (0, 0))

while hq:
    start, drive = heappop(hq)

    if distance[start] < drive:
        continue

    for dest, dist in graph[start]:
        if drive + dist < distance[dest]:
            distance[dest] = drive + dist
            heappush(hq, (dest, drive + dist))

print(distance[d])
