n = int(input())
row = [0]*n
cnt = 0


def n_queen(depth):
    global cnt
    if depth == n:
        cnt += 1

    else:
        for i in range(n):
            row[depth] = i
            if check(depth):
                n_queen(depth+1)


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True


n_queen(0)
print(cnt)