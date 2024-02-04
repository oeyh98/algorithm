import sys

n, c = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(n)]

x.sort()
start, end = 1, x[-1]
result = 0

while start <= end:
    mid = (start+end) // 2
    current = x[0]
    cnt = 1

    for i in range(1, n):
        if x[i] - current >= mid:
            cnt += 1
            current = x[i]
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
