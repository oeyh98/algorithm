n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
idx = n - 1
while k:
    if k < coins[idx]:
       idx -= 1
    else:
        tmp = int(k/coins[idx])
        k = k - (coins[idx]*tmp)
        cnt += tmp
print(cnt)
