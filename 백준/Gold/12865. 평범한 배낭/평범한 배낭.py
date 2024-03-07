n, k = map(int, input().split())
items = [(0, 0)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

for i in range(n+1):
    for j in range(k+1):
        w, v = items[i]
        if w <= j:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])