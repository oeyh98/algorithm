n, score, p = map(int, input().split())

if n:
    rank = list(map(int, input().split()))

    if n == p and rank[-1] >= score:
        result = -1
    else:
        result = n+1
        for i in range(n):
            if rank[i] <= score:
                result = i + 1
                break
else:
    result = 1

print(result)
