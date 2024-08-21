from heapq import heappush, heappop
INF = int(1e9)

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    hq = []
    k = 1
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
         
    distance[k] = 0
    heappush(hq, (0, k))
    
    while hq:
        weight, node = heappop(hq)

        if distance[node] < weight:
            continue
        
        for dest in graph[node]:
            dist = weight + 1
            if dist < distance[dest]:
                distance[dest] = dist
                heappush(hq, (dist, dest))
    
    max_value = 0
    answer = 1
    for d in distance[0:]:
        if d != INF:
            if max_value < d:
                answer = 1
                max_value = d
            elif max_value == d:
                answer += 1
        
        
    return answer 