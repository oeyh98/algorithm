from collections import deque

def solution(n, computers):
    answer = 0
    n  = len(computers)
    visited = [False] * n
    
    def dfs(cur, computers):
        dq = deque()
        dq.append(cur)
        
        while dq:
            node = dq.popleft()
            visited[node] = True
            
            for i in range(n):
                if computers[node][i] and not visited[i]:
                    dq.append(i)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, computers)
            
    
    return answer