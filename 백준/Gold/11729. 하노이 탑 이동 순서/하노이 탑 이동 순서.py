n = int(input())
result = []

def hanoi(tower, start, end, serve):
    global result
    if tower == 1:
        result.append((start, end))
        return

    hanoi(tower-1, start, serve, end)
    result.append((start, end))
    hanoi(tower-1, serve, end, start)


hanoi(n, 1, 3, 2)
print(len(result))
for i, j in result:
    print(i, j)