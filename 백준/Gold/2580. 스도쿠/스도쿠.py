def check(x, y, n):
    for i in range(9):
        if sudoku[y][i] == n or sudoku[i][x] == n:
            return False

    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if sudoku[ny + i][nx + j] == n:
                return False
    return True


def dfs(depth):
    if depth == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit()

    x = blank[depth][1]
    y = blank[depth][0]

    for i in range(1, 10):
        if check(x, y, i):
            sudoku[y][x] = i
            dfs(depth + 1)
            sudoku[y][x] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
start = 0

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])

dfs(start)