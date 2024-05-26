import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 9시, 10.5시, 12시, 1.5시, 3시, 4.5시, 6시, 7.5시
# d ix -1 해줘야 됨.
# d의 대각선 : 1, 3, 5, 7
rx = [0, -1, -1, -1, 0, 1, 1, 1]
ry = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for direction in directions:
    d, m = direction[0] - 1, direction[1] % N
    not_cloud = set()
    while clouds:
        x, y = clouds.pop()
        nx, ny = (x + m*rx[d]) % N, (y + m*ry[d]) % N
        graph[nx][ny] += 1
        # 구름이 있던 자리는 저장해뒀다가 나중에 제외 시켜줌
        not_cloud.add((nx, ny))

    # 물 뿌리기 (주의) 이 행동은 먼저 비가 내린 뒤 진행해야됨.
    for nx, ny in not_cloud:
        count = 0
        for _ in range(1, 8, 2):
            nnx = nx + rx[_]
            nny = ny + ry[_]
            if 0 <= nnx < N and 0 <= nny < N:
                if graph[nnx][nny]:
                    count += 1
        graph[nx][ny] += count
    # 새로운 구름 생성
    for x in range(N):
        for y in range(N):
            # 기존 구름 있던 자리가 아니고
            if (x, y) not in not_cloud:
                # 물의 양이 2 이상인 곳 구름 생성 후 물 양 줄이기
                if graph[x][y] >= 2:
                    clouds.append((x, y))
                    graph[x][y] -= 2

print(sum([sum(_) for _ in graph]))