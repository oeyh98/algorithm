def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for win, defeat in results:
        graph[win][defeat] = 1
        graph[defeat][win] = -1

    for node in range(1, n+1):
        for i in range(1, n+1):
            if graph[node][i] == 1:
                for j in range(1, n+1):
                    if graph[i][j] == 1:
                        graph[node][j] = 1
                        graph[j][node] = -1
            elif graph[node][i] == -1:
                for j in range(1, n+1):
                    if graph[i][j] == -1:
                        graph[node][j] = -1
                        graph[j][node] = 1

    for i in range(1, n+1):
        temp = 0
        for j in range(1, n+1):
            if (i != j) and (graph[i][j] == 1 or graph[i][j] == -1):
                temp += 1
                
        if temp == n - 1:
            answer += 1
            
    print(graph)
    return answer