def solution(n, k, enemy):
    answer = []
    def dfs(cnt, n, k, enemy):
        if k == 0 and n < enemy[0]:
            answer.append(cnt)
            
        if len(enemy) > 1:
            if k > 0:
                dfs(cnt+1, n, k-1, enemy[1:])
            if n >= enemy[0]:
                dfs(cnt+1, n - enemy[0], k, enemy[1:])
        
    dfs(0, n, k, enemy)

    return answer