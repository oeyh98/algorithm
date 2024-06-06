n, m = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, m * min(a)

while start <= end:
    mid = int((start + end) / 2)
    tmp = 0

    for i in a:
        tmp += (mid // i)

    if tmp < m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)