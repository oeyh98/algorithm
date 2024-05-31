from collections import deque

stone = [0] * 100001
a, b, n, m = map(int, input().split())

dx = [-1, 1, (-1)*a, a, (-1)*b, b]

dq = deque()
cnt = 0

dq.append(n)
stone[n] = 0

while dq:
    x = dq.popleft()
    if x == m:
        print(stone[x])
        exit()

    for i in range(6):
        nx = x + dx[i]

        if 0 <= nx < 100001:
            if stone[nx] == 0:
                dq.append(nx)
                stone[nx] = stone[x] + 1

    nx = x * a
    if 0 <= nx < 100001:
        if stone[nx] == 0:
            dq.append(nx)
            stone[nx] = stone[x] + 1
    nx = x * b
    if 0 <= nx < 100001:
        if stone[nx] == 0:
            dq.append(nx)
            stone[nx] = stone[x] + 1



