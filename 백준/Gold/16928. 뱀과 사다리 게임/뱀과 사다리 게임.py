from collections import deque
n, m = map(int, input().split()) #n은 올라가는 사다리, m은 내려가는 뱀
graph = [i for i in range(1, 101)]
visit = [0 for i in range(1, 101)]
move = []

for i in range(n+m):
    move.append(list(map(int, input().split())))
move.sort()


def sal(x):
    for m in move:
        if m[0] == x:
            return m[1]
    return x


def bfs():
    q = deque()
    q.append(1)

    while q:
        x = q.popleft()

        for i in range(1, 7):
            nx = x + i
            nx = sal(nx)

            if nx == 100:

                return visit[x] + 1
            elif 0 < nx < 100 and visit[nx] == 0:
                q.append(nx)
                visit[nx] = visit[x] + 1


print(bfs())

