n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

def dfs(depth, total, pl, mi, mu, di):
    global max_value, min_value

    if depth == n:
        max_value = max(total, max_value)
        min_value = min(total, min_value)

    if pl:
        dfs(depth+1, total + a[depth], pl - 1, mi, mu, di)
    if mi:
        dfs(depth + 1, total - a[depth], pl, mi - 1, mu, di)
    if mu:
        dfs(depth + 1, total * a[depth], pl, mi, mu - 1, di)
    if di:
        dfs(depth + 1, int(total / a[depth]), pl, mi, mu, di - 1)


dfs(1, a[0], op[0], op[1], op[2], op[3])
print(max_value)
print(min_value)