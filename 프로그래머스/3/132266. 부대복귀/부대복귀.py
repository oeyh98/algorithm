from collections import deque
INF = int(1e9)

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
         
    distance = [INF] * (n + 1)
    distance[destination] = 0
        
    dq = deque([destination])
    
        
    while dq:
        cur = dq.popleft()

        for node in graph[cur]:
            if distance[node] == INF:    
                dq.append(node)
                distance[node] = distance[cur] + 1


    
    answer = []
    for source in sources:
        answer.append(distance[source] if distance[source] != INF else -1)

    return answer
