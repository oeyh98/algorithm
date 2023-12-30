n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(n - 2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
            card_sum = arr[i] + arr[j] + arr[k]
            if result < card_sum <= m:
                result = card_sum

print(result)
