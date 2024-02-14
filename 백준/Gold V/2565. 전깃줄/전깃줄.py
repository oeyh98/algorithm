n = int(input())
ab = [[0, 0]] * n
dp = [1] * n
for i in range(n):
    ab[i] = list(map(int, input().split()))

ab.sort(key=lambda x:x[0])

for i in range(1, n):
    for j in range(i):
        if ab[i][1] > ab[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
