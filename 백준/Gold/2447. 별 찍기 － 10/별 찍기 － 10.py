def star(n):
    if n == 3:
        return ['***', "* *", "***"]

    arr = star(n//3)
    stars = []

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i + ' '*(n//3) + i)
    for i in arr:
        stars.append(i * 3)

    return stars

n = int(input())
print('\n'.join(star(n)))