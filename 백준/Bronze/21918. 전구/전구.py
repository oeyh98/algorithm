def control(a, b, c):
    if a == 1:
        bulb[b] = c
    elif a == 2:
        for i in range(b, c):
            bulb[i] = 0 if bulb[i] == 1 else 1
    elif a == 3:
        bulb[b:c] = [0] * (c - b)
    elif a == 4:
        bulb[b:c] = [1] * (c - b)


n, m = map(int, input().split())
bulb = list(map(int, input().split()))
for i in range(m):
    a, b, c = map(int, input().split())
    control(a, b - 1, c)

print(*bulb)