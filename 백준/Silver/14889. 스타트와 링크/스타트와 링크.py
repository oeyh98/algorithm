n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = n//2
ans = 1e9


def team_sum(start, link):
    s_sum, l_sum = 0, 0
    for i in range(m):
        for j in range(m):
            s_sum += arr[start[i]][start[j]]
            l_sum += arr[link[i]][link[j]]
    return abs(s_sum - l_sum)


def dfs(p_num, start, link):
    global ans
    if p_num == n:
        if len(start) == len(link):
            ans = min(ans, team_sum(start, link))
        return

    dfs(p_num + 1, start+[p_num], link)
    dfs(p_num + 1, start, link+[p_num])


dfs(0, [], [])
print(ans)