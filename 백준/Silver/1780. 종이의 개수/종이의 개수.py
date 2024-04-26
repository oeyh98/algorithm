n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0]


def check_color(c_start, c_end, r_start, r_end, color):
    for i in range(r_start, r_end + 1):
        for j in range(c_start, c_end + 1):
            if graph[i][j] != color:
                return False
    return True


def bin_search(c_start, c_end, r_start, r_end):
    global answer

    if check_color(c_start, c_end, r_start, r_end, graph[r_start][c_start]):
        if graph[r_start][c_start] == -1:
            answer[0] += 1
        elif graph[r_start][c_start] == 0:
            answer[1] += 1
        else:
            answer[2] += 1
    else:
        c_third = (c_end - c_start + 1) // 3
        r_third = (r_end - r_start + 1) // 3

        # 9개 구역으로 나누어 재귀 호출
        for i in range(3):
            for j in range(3):
                new_c_start = c_start + i * c_third
                new_c_end = new_c_start + c_third - 1
                new_r_start = r_start + j * r_third
                new_r_end = new_r_start + r_third - 1
                if new_c_end >= c_end: new_c_end = c_end
                if new_r_end >= r_end: new_r_end = r_end
                bin_search(new_c_start, new_c_end, new_r_start, new_r_end)


bin_search(0, n - 1, 0, n - 1)

print(*answer, sep="\n")

