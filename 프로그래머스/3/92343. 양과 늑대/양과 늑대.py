def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1
    
    def dfs(sheep, wolf):
        if wolf >= sheep:
            return
        else:
            answer.append(sheep)

        for parent, child in edges:
            if visited[parent] == 1 and visited[child] == 0:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[child] = 0
                
    dfs(1, 0)
    return max(answer)