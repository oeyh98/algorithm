t = int(input())
n = [int(input()) for _ in range(t)]

max_value = max(n)
dp = [0] * (max_value+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_value + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for num in n:
    print(dp[num])