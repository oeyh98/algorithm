def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[2] = 3
    
    for i in range(4, n+1, 2):
        dp[i] = (dp[i-2] * 4 - dp[i-4]) % 1000000007
        
        
    return dp[n] 

#[0, 0, 3, 0, 11, 0, 61, 0, 153, 571]



