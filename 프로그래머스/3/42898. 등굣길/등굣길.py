def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m+1) for _ in range(n+1)]
    for x, y in puddles:
        dp[y][x] = -1
        
    dp[1][1] = 1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1 or (i == 1 and j == 1):
                continue
                
            else:
                from_up, from_left = 0, 0
                if dp[i-1][j] != -1:
                    from_up += dp[i-1][j] 
                if dp[i][j-1] != -1:
                    from_left += dp[i][j-1] 
                
                dp[i][j] = (from_up + from_left) % MOD
            
    return dp[n][m]