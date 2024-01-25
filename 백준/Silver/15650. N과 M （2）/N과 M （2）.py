n, m = map(int, input().split())
result = []
def back():
    if len(result) == m:
        print(*result, end=' ')
        print()
        return

    for i in range(1, n+1):
        if i not in result:
            if len(result) == 0 or (result and result[-1] < i):
                result.append(i)
                back()
                result.pop()

back()
