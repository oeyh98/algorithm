n, m = map(int, input().split())
lamp = [0] * (m+1)
lamp[0] = 1
switch = []

for _ in range(n):
    order = list(map(int, input().split()))[1:]
    switch.append(order)

    for i in order:
        lamp[i] += 1

def off_lamp(l, s):
    for i in s:
        l[i] -= 1

    return True if 0 not in l else False


for s in switch:
    result = off_lamp(lamp[:], s)
    if result:
        print(1)
        exit()
print(0)

