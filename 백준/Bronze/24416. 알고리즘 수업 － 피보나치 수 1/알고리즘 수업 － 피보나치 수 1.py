n = int(input())
dp_cnt = 0
def dp(n):
    dp_cnt = 0

    f = [0 for _ in range(n)]
    f[0] = 1
    f[1] = 1
    for i in range(2, n):
        dp_cnt += 1
        f[i] = f[i-1] + f[i-2]
    return f[n-1], dp_cnt


f, d = dp(n)
print(f, d)
