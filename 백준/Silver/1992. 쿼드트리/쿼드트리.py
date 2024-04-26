n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
answer = []


def check_color(c_start, c_end, r_start, r_end, color):
    for i in range(r_start, r_end + 1):
        for j in range(c_start, c_end + 1):
            if graph[i][j] != color:
                return False
    return True


def bin_search(c_start, c_end, r_start, r_end):
    global answer

    if check_color(c_start, c_end, r_start, r_end, graph[r_start][c_start]):
        if graph[r_start][c_start] == 1:
            answer.append("1")
        else:
            answer.append("0")
    else:
        c_mid = (c_start + c_end) // 2
        r_mid = (r_start + r_end) // 2

        answer.append("(")
        bin_search(c_start, c_mid, r_start, r_mid) # 좌상
        bin_search(c_mid + 1, c_end, r_start, r_mid) # 우상
        bin_search(c_start, c_mid, r_mid + 1, r_end) # 좌하
        bin_search(c_mid + 1, c_end, r_mid + 1, r_end) # 우하
        answer.append(")")


bin_search(0, n - 1, 0, n - 1)

print("".join(answer))

